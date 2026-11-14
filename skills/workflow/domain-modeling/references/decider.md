# Decider templates

Reference for [`domain-modeling`](../SKILL.md). One aggregate, a seat, in
three languages. Commands, events, rejections and states are closed, so the
compiler or type checker rejects an unhandled case.

## Java (21+)

```java
sealed interface SeatCommand permits ReserveSeat, ReleaseSeat {}
record ReserveSeat(String customer) implements SeatCommand {}
record ReleaseSeat() implements SeatCommand {}

sealed interface SeatEvent permits SeatReserved, SeatReleased {}
record SeatReserved(String customer) implements SeatEvent {}
record SeatReleased() implements SeatEvent {}

sealed interface SeatRejection permits SeatAlreadyTaken, SeatNotReserved {}
record SeatAlreadyTaken() implements SeatRejection {}
record SeatNotReserved() implements SeatRejection {}

sealed interface SeatState permits Available, Reserved {}
record Available() implements SeatState {}
record Reserved(String customer) implements SeatState {}

sealed interface SeatDecision permits Accepted, Rejected {}
record Accepted(java.util.List<SeatEvent> events) implements SeatDecision {}
record Rejected(SeatRejection rejection) implements SeatDecision {}

final class Seat {
    static SeatDecision decide(SeatCommand command, SeatState state) {
        return switch (command) {
            case ReserveSeat c -> switch (state) {
                case Available a -> new Accepted(java.util.List.of(new SeatReserved(c.customer())));
                case Reserved r -> new Rejected(new SeatAlreadyTaken());
            };
            case ReleaseSeat c -> switch (state) {
                case Reserved r -> new Accepted(java.util.List.of(new SeatReleased()));
                case Available a -> new Rejected(new SeatNotReserved());
            };
        };
    }

    static SeatState evolve(SeatState state, SeatEvent event) {
        return switch (event) {
            case SeatReserved e -> new Reserved(e.customer());
            case SeatReleased e -> new Available();
        };
    }
}
```

## TypeScript

```ts
type SeatCommand = { type: "ReserveSeat"; customer: string } | { type: "ReleaseSeat" };
type SeatEvent = { type: "SeatReserved"; customer: string } | { type: "SeatReleased" };
type SeatRejection = { type: "SeatAlreadyTaken" } | { type: "SeatNotReserved" };
type SeatState = { status: "available" } | { status: "reserved"; customer: string };
type SeatDecision =
  | { ok: true; events: SeatEvent[] }
  | { ok: false; rejection: SeatRejection };

export function decide(command: SeatCommand, state: SeatState): SeatDecision {
  switch (command.type) {
    case "ReserveSeat":
      return state.status === "available"
        ? { ok: true, events: [{ type: "SeatReserved", customer: command.customer }] }
        : { ok: false, rejection: { type: "SeatAlreadyTaken" } };
    case "ReleaseSeat":
      return state.status === "reserved"
        ? { ok: true, events: [{ type: "SeatReleased" }] }
        : { ok: false, rejection: { type: "SeatNotReserved" } };
    default:
      return command satisfies never;
  }
}

export function evolve(state: SeatState, event: SeatEvent): SeatState {
  switch (event.type) {
    case "SeatReserved":
      return { status: "reserved", customer: event.customer };
    case "SeatReleased":
      return { status: "available" };
    default:
      return event satisfies never;
  }
}
```

## Python (3.12+, checked with pyright or mypy)

```python
from dataclasses import dataclass
from typing import assert_never


@dataclass(frozen=True)
class ReserveSeat:
    customer: str

@dataclass(frozen=True)
class ReleaseSeat: ...

@dataclass(frozen=True)
class SeatReserved:
    customer: str

@dataclass(frozen=True)
class SeatReleased: ...

@dataclass(frozen=True)
class SeatAlreadyTaken: ...

@dataclass(frozen=True)
class SeatNotReserved: ...

@dataclass(frozen=True)
class Available: ...

@dataclass(frozen=True)
class Reserved:
    customer: str

type SeatCommand = ReserveSeat | ReleaseSeat
type SeatEvent = SeatReserved | SeatReleased
type SeatRejection = SeatAlreadyTaken | SeatNotReserved
type SeatState = Available | Reserved


def decide(command: SeatCommand, state: SeatState) -> list[SeatEvent] | SeatRejection:
    match command:
        case ReserveSeat(customer=customer):
            return [SeatReserved(customer)] if isinstance(state, Available) else SeatAlreadyTaken()
        case ReleaseSeat():
            return [SeatReleased()] if isinstance(state, Reserved) else SeatNotReserved()
        case _:
            assert_never(command)


def evolve(state: SeatState, event: SeatEvent) -> SeatState:
    match event:
        case SeatReserved(customer=customer):
            return Reserved(customer)
        case SeatReleased():
            return Available()
        case _:
            assert_never(event)
```

## Application service

The service is the only place with I/O, and it holds no business rule:

```text
state     = repository.load(id)            # state-stored, or fold(evolve, initial, stored events)
decision  = decide(command, state)
on rejection: return it to the caller
on events:    newState = fold(evolve, state, events)
              repository.save(id, newState)  # or append the events
              publish(events)                # only events with a consumer
```

Load, save and publish run inside one transaction. Event sourcing replaces
`save` with appending events and `load` with a fold over them; `decide` and
`evolve` stay the same.
