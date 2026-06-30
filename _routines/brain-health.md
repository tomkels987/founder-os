# Routine — Brain-health (the self-audit)

> **Invocation:** scheduled weekly + on-demand whenever something feels off.
> **Why it exists:** every operating system has the same failure mode — state files go stale, facts drift, links break, two files start quietly disagreeing. This routine sweeps for rot **before** it poisons a decision. It's the OS auditing itself.

---

## What it checks

Run the whole brain through these checks. Report findings, **don't auto-fix** the judgement calls — surface them.

1. **Stale files.** Any canonical file (`OKRS.md`, `CONTROL_CENTRE.md`, the CRM) not updated in longer than its expected cadence. Flag with how stale.
2. **Source-of-truth drift.** For each fact-type in `SOURCES_OF_TRUTH.md`, confirm the derived views still match the canonical source. Where the scorecard and the CRM disagree about the same fact → 🔴 **conflict**: show **both sides, don't pick a winner**, ask the founder.
3. **Provenance gaps.** Any "fact" in a canonical file with no source + date stamp (per `INGESTION_GATE.md`). A fact you can't trace is a fact you can't trust.
4. **Unverified flatter still parked.** Any `[unverified]` flattering number that's been sitting unvalidated — surface it for a tier-1/2 check.
5. **Broken internal links.** Any `.md` link or file reference pointing at something that no longer exists.
6. **Orphans.** Research or notes never indexed in their tracker; files no routine reads.
7. **Routine health.** Any routine in `SCHEDULE.md` marked registered but with no recent run in `_routines/runs/` — it may have silently stopped firing.
8. **Doc/export drift.** If you keep generated exports (e.g. `.docx` from `.md`), flag any export older than its source.

---

## Output

```
🩺 Brain-health — [date]

🔴 Must fix (conflicts, broken truth)
- [finding] → [where] → [the question for you]

🟡 Should fix (stale, missing provenance, orphans)
- [finding] → [where]

🟢 Clean
- [what passed]
```

- Save the full report to `_memory/brain-health/YYYY-MM-DD.md`, commit `os/auto:`, push.
- **Escalate (notify) only if there's a 🔴 finding** — a real conflict or broken truth. 🟡 items wait for the report.
- **Never auto-resolve a conflict.** On any clash, the rule holds: surface both sides, the founder decides. **Never outbound, never money.**
