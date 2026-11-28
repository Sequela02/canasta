# Sources and their copies

For a canonical file and the generated or synced copies made from it: build
settings, editor settings, agent instructions, installed files, generated docs.
A copy is never a second source of truth. Review; change nothing.

1. **List sources and copies.** Find the source files, the generator or sync
   command, and each copy. Use the project's own status command if it has one.
   Otherwise read the files and say what you couldn't check. A matching file
   name alone doesn't show who owns a file.
2. **Classify each copy** as current, stale (source changed), drifted (someone
   edited the copy), missing or unmanaged, and record the evidence: both
   digests, the revision, or the diff.

   ```text
   source  config/base.json        rev a1b2c3
   copy    .tool/settings.json     drifted   (line 14 edited by hand)
   copy    ~/.tool/settings.json   stale     (built from rev 9f8e7d)
   copy    other/settings.json     unmanaged (no generator mentions it)
   ```

3. **Separate a wrong source from a wrong sync.** A bad value in the source is a
   source fix; a copy that fell behind is a sync fix. Don't hand-edit a copy to
   hide a source defect.
4. **Recommend the narrow fix:** correct the source if needed, preview the
   diff of each copy, then sync only the copies the owner picks. Recheck source
   and target right before applying so an old approval can't overwrite newer
   work. Stop and say why when ownership is unclear, the source is invalid,
   the list is incomplete or a safe merge isn't established.
5. **Report per copy.** Give findings first, then an overall status: valid,
   needs_changes or blocked. One unreadable copy means you can't call the
   whole set in sync. A recommended repair is not permission to run it.
