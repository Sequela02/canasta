# Integration

Reference for [`domain-modeling`](../SKILL.md): what happens around a
decider when a command is retried, two writers race, a side effect leaves the
database, a flow spans aggregates, or a client works offline. The SQL is
PostgreSQL. Add each pattern when its risk exists, not by default; a team of
one to three people pays for every moving part.

## Idempotency

Every command that moves money or inventory carries an idempotency key. The
key is claimed in the same transaction as the business write, under a unique
constraint, so a retry returns the first result instead of acting twice.

```sql
CREATE TABLE idempotency_key (
  scope        text        NOT NULL,          -- the command or endpoint
  key          text        NOT NULL,
  request_hash text        NOT NULL,
  response     jsonb,
  created_at   timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (scope, key)
);

-- In the command's transaction, before the business write:
INSERT INTO idempotency_key (scope, key, request_hash)
VALUES ($1, $2, $3)
ON CONFLICT (scope, key) DO NOTHING
RETURNING key;
-- A row back: first attempt. Run decide, save, then in the same transaction:
UPDATE idempotency_key SET response = $4 WHERE scope = $1 AND key = $2;
-- No row back: a retry. Return the stored response, or reject it when
-- request_hash differs (the same key reused for a different request).

-- Expiry, on a schedule:
DELETE FROM idempotency_key WHERE created_at < now() - interval '7 days';
```

A concurrent retry blocks on the insert until the first transaction commits,
then finds the key. The client creates the key once per operation and reuses
it on every retry.

**Webhooks** deduplicate on the provider's event id, in the transaction that
applies the change; a reconciliation job catches webhooks that never arrive.

```sql
CREATE TABLE processed_event (
  provider    text        NOT NULL,
  event_id    text        NOT NULL,
  received_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (provider, event_id)
);
INSERT INTO processed_event (provider, event_id) VALUES ($1, $2)
ON CONFLICT DO NOTHING RETURNING event_id;  -- no row back: already applied
```

**Check:** a test sends the same command, and the same webhook, twice and
asserts one effect.

## Optimistic concurrency

Each aggregate row carries a version. The save succeeds only against the
version that was loaded; zero rows updated is a conflict.

```sql
UPDATE seat SET status = $2, customer = $3, version = version + 1
WHERE id = $1 AND version = $4;
```

For scarce inventory, such as a seat, a conditional update on the state is
the guard, because a lost seat is not worth retrying:

```sql
UPDATE seat SET status = 'held', customer = $2
WHERE id = $1 AND status = 'available';
```

Show a conflict to the person with the current state ("another register took
this seat") and refresh; retry automatically only conflicts that a fresh
`decide` can resolve.

**Check:** a test runs two writers against the same version or the same seat
and asserts that exactly one succeeds.

## Transactional outbox

A side effect outside the database (a message, an email, a webhook to another
system, waking a worker) is written as an outbox row in the same transaction
as the state. A relay delivers it afterwards, at least once, so every
consumer is idempotent; the outbox `id` is its idempotency key.

```sql
CREATE TABLE outbox (
  id           bigint      GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  aggregate_id text        NOT NULL,
  type         text        NOT NULL,
  payload      jsonb       NOT NULL,
  attempts     int         NOT NULL DEFAULT 0,
  available_at timestamptz NOT NULL DEFAULT now(),
  created_at   timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX outbox_available ON outbox (available_at, id);

CREATE TABLE outbox_dead (
  id           bigint      PRIMARY KEY,
  aggregate_id text        NOT NULL,
  type         text        NOT NULL,
  payload      jsonb       NOT NULL,
  attempts     int         NOT NULL,
  created_at   timestamptz NOT NULL,
  failed_at    timestamptz NOT NULL DEFAULT now(),
  error        text
);
```

The relay claims a small batch per transaction, so several relays never take
the same row:

```sql
SELECT id, type, payload FROM outbox
WHERE available_at <= now()
ORDER BY id
LIMIT 20
FOR UPDATE SKIP LOCKED;

-- Delivered:
DELETE FROM outbox WHERE id = ANY($1);

-- Failed: back off.
UPDATE outbox
SET attempts = attempts + 1,
    available_at = now() + make_interval(secs => least(3600, power(2, attempts + 1)))
WHERE id = $1;

-- Failed too often: move to dead letter, so one bad row does not block the rest.
WITH dead AS (
  DELETE FROM outbox WHERE id = $1
  RETURNING id, aggregate_id, type, payload, attempts, created_at
)
INSERT INTO outbox_dead (id, aggregate_id, type, payload, attempts, created_at, error)
SELECT id, aggregate_id, type, payload, attempts, created_at, $2 FROM dead;
```

- Delete delivered rows instead of marking them, and watch the table's size;
  dead tuples and long transactions are the usual way an outbox slows down.
- Keep the claiming transaction short: bound each delivery with a timeout.
- When consumers need per-aggregate order, run one relay, or claim only the
  oldest row of each `aggregate_id`.
- `LISTEN`/`NOTIFY` may wake the relay sooner; polling stays the guarantee.
- In Spring Modulith, the event publication registry is this outbox: enable
  republishing incomplete publications on restart and remove completed ones,
  using the property names of the Modulith version in use. A Postgres job
  queue that enqueues inside the caller's transaction (Graphile Worker,
  pg-boss) plays the same role in Node.

Where losing a side effect is tolerable, publishing after commit with a
reconciliation job is the simpler choice; say so in the pull request.

**Check:** an architecture test lets only the relay depend on the sending
clients; a test commits, stops the process before delivery, restarts it, and
asserts the side effect happens once.

## Process manager

A flow across aggregates (hold seats, charge, confirm; release on failure) is
its own decider: an explicit state type with a case per step and a deadline
for every wait, driven by events delivered through the outbox.

```text
Holding --SeatsHeld--> Charging --PaymentSucceeded--> Confirmed
                          |--PaymentFailed or deadline--> Releasing --SeatsReleased--> Released
```

Each step is idempotent and each failure has a named compensation. Before
writing an engine for long or many-step flows, evaluate a durable-execution
library that runs on the existing Postgres; a separate workflow cluster is
the last option for a small team.

**Check:** property tests drive the flow with events in any order, duplicated
and late, and assert it always ends confirmed or released.

## Offline clients

A client that must keep working without a connection writes each operation
to a local queue (SQLite or IndexedDB) in the same local transaction as its
local effect:

- the client generates the entity id (a UUID) and one idempotency key per
  operation;
- sync pushes the queue in order; the server applies each operation with its
  idempotency key and a conditional check against current state;
- a rejected operation is marked failed and shown to staff, never dropped;
- inventory is a ledger of movements, not one mutable quantity, so offline
  sales merge by appending; scarce items sold offline come from blocks
  allocated to the device beforehand;
- prices and catalog are server-authoritative; the price the customer saw is
  honored.

Use a sync engine only when several devices edit the same records offline;
a queue with server authority covers a single register.

**Check:** a sync test replays a duplicated operation and an operation
interrupted mid-push, and asserts one effect each.
