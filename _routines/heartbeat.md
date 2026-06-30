# Routine — Weekly Heartbeat

> **Fires:** weekly (e.g. Monday AM), on the always-on machine.
> **Output:** refresh `OKRS.md` + the top of `CONTROL_CENTRE.md`; a digest to `_routines/runs/`; a ≤250-word scan in chat.

---

## Prompt

You are running the **Weekly Heartbeat**. The whole job is the three goals (the OKRs) and the keystone chain — which goal unlocks the others. First, **`git pull --rebase --autostash`** to act on the latest state. Then read, in order:

1. `OKRS.md` — the scorecard you're about to refresh.
2. The most recent digests in `_routines/runs/`.
3. `CONTROL_CENTRE.md` — the current first-stop.
4. `_crm/` — for aging threads and unmade decisions.
5. The latest few transcripts — to ground in what just happened.
6. `_memory/patterns/` — carry forward the lessons.

Produce this brief:

```
☀ Weekly Heartbeat — [date]

🎯 The scorecard
- O1 [name]: [where it stands] · [on/off track] · [days left] → one move: [...]
- O2 [name]: [where it stands] · [on/off track] · [days left] → one move: [...]
- O3 [name]: [where it stands] → one move: [...]

⚠ Needs you this week (only two classes)
- Unmade decision: [decision] — [why it can't wait]
- Aging keystone thread: [who] [n] days cold — [a chase is drafted]

💡 One thing you might be missing
[the signal across the goals/transcripts not yet given explicit treatment]
```

## Rules
- **Refresh, don't just report.** Update the standing lines in `OKRS.md` and the banner at the top of `CONTROL_CENTRE.md` to current truth. These are mutations — commit them `os/auto:`.
- **Escalate only two classes:** the unmade decision and the aging keystone thread.
- **No false momentum.** If a goal is off track, say so plainly. The Heartbeat's job is to make off-track-ness impossible to ignore.
- **Never outbound, never money.** Drafts only — you fire send.
- If `OKRS.md` was last refreshed more than a week ago, flag it 🚨 at the top.
- If a transcript surfaced a new person not in `_crm/`, **propose** adding them — don't auto-add people. (Scorecard/timestamp refreshes are automatic; adding a person to the CRM stays a proposal you approve.)

## On completion
1. Write `OKRS.md` + the `CONTROL_CENTRE.md` banner to current state. Commit `os/auto: weekly heartbeat [date]`, push.
2. Digest → `_routines/runs/YYYY-MM-DD-heartbeat.md`, commit, push.
3. Notify only if a goal newly projects off-target against its date, or a gate just tripped.
