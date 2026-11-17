> Reference for `documentation-hygiene`.

# Repository Audit

Use this reference when a task asks whether an existing repository holds only
its own system, before onboarding someone to it, or before making it public.
Audit the default branch read-only, then propose changes as their own work.

1. **Scan.** Search tracked files for the names that shouldn't be there: other
   projects, clients and people of the organization, its hostnames, accounts and
   secret-store names, absolute user paths, and email addresses outside reserved
   domains. A name list finds only what someone thought to list, so also read
   the documentation entry points, design documents, test fixtures and captured
   artifacts (test reports, logs, snapshots) whole.
2. **Read every hit in context** and classify it as keep, rewrite, move or
   remove. Most hits from a name list are noise. Keep:
   - a dependency on another of the organization's products: it is part of
     this system;
   - domain vocabulary that resembles sensitive topics, such as prices in a
     sales system;
   - third-party license and copyright notices, authors' emails included;
   - reserved example domains and invented names;
   - the repository's own product and, in a private client repository, its
     client.
   A mention of an organization-wide standard is a judgment call: keep the
   rule the reader must follow, stated in the repository, and drop the pointer
   when the reader can't open its target.
3. **Record** each finding with its file and line, the decision and, for a move,
   the destination. Material already published stays in history and in any
   copy made of it: rotate an exposed credential at once, and leave a history
   rewrite to the owner.
4. **Close** by rerunning the scan: every remaining hit is one recorded as kept.
