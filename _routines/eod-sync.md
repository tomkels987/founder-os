# Routine — End-of-day sync (laptop → always-on machine)

> **Fires:** daily (e.g. ~22:00), **laptop only**.
> **Why it exists:** the always-on machine runs the continuous OS off its own git clone. Anything you did on the laptop today — edits, new transcripts dropped in, CRM updates — has to reach it, or its routines act on stale state. This pushes the day's work so the always-on machine wakes up current.

---

## What it does
1. `git add -A`
2. If there's anything to commit: `git commit -m "os/auto: end-of-day laptop sync <date>"`
3. `git push origin main`
4. If nothing changed, do nothing (no empty commits).

## Rules
- **Safe + idempotent:** only commits when there are real changes; never force-pushes.
- **Pairs with pull-first on the always-on machine:** every routine there begins with `git pull --rebase --autostash`, so the two machines converge through `main`.
- **`os/auto:` prefix** keeps these checkpoint commits easy to spot and `git revert`-able.
- If a push fails on a conflict (you also edited on the other machine), it **surfaces the conflict for you** rather than forcing — the repo is the source of truth.

## Note
This is a blunt daily checkpoint — it commits whatever's in the tree, including work-in-progress. That's the intended trade: never lose a day's work, never leave the other machine stale. Conscious, structured commits (a finished doc, a logged decision) you still make yourself with a real message.

*(If you run a single machine, you don't need this routine — git-commit your work normally.)*
