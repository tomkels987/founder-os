# Routine — Weekly review

> **Fires:** weekly (e.g. Friday PM), on the always-on machine.
> **Output:** a short "what moved per goal this week" digest + a drafted update you can send, to `_routines/runs/`.
> **Why it exists:** the heartbeat looks *forward* (what's the move next week). This looks *back* — it reads the week's runs and says, plainly, what actually moved on each goal, and hands you a draft update you can fire to a co-founder, an advisor, or yourself. It closes the week.

---

## Step 0 — Context pull (before any reasoning)

First, **`git pull --rebase --autostash`** to act on the latest state. Then read, in order:

1. `OKRS.md` — the three goals you're reporting against.
2. **Every digest in `_routines/runs/` from the last 7 days** — the heartbeat, sync, cabinet runs are the raw record of what happened.
3. `_crm/` — for any state that changed (a stage moved, a thread went cold or warm).
4. `decisions/DECISIONS.md` — anything decided this week.

## Step 1 — Derive what moved

For each objective, answer in one line: **what actually changed this week, and is it on or off track?** Movement is concrete (a stage changed, a thing shipped, a number ticked) — not activity ("had three calls" is not movement). If nothing moved on a goal, say so plainly; a flat week is a signal.

## Step 2 — Draft the update

Draft a short update someone could actually read — the kind you'd send a co-founder or advisor, or keep for yourself. Plain, honest, no false momentum.

## Output

```
🗓 Weekly review — [date]

📈 What moved this week
- O1 [name]: [what changed] · [on/off track]
- O2 [name]: [what changed] · [on/off track]
- O3 [name]: [what changed] · [on/off track]

🟰 What didn't
- [any goal that was flat — named, not hidden]

✍️ Drafted update (yours to send or keep)
[3–6 lines, plain and honest]
```

## Rules

- **Surfaces nothing urgent.** This is a backward-looking close-of-week — escalation is the heartbeat's and the sync's job, not this one. If something genuinely can't wait, it belongs in those routines, not here.
- **Never sends.** The update is a **draft**. You fire it, or you don't.
- **No false momentum.** A flat week is reported as a flat week. The value is honesty, not cheerleading.
- **Reads, doesn't re-derive the scorecard.** The heartbeat owns refreshing `OKRS.md`. This routine reads the standing lines; it doesn't recompute them.

## On completion

1. Digest + drafted update → `_routines/runs/YYYY-MM-DD-review.md`, commit `os/auto: weekly review [date]`, push.
2. No notification unless asked — the draft is waiting when you next open the app.
