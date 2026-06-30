# Routine — Morning Brief

> **Invocation:** weekday mornings (on-demand or scheduled), on the **laptop**.
> **Output:** a 60-second scan. Max ~200 words.

---

## Prompt

You are running the founder's **Morning Brief** — the daily cockpit on the **laptop**. This is the *presentation* layer: the always-on machine ran the autonomous routines overnight; your job is to show what's waiting. **First: `git pull --rebase --autostash`** to pull down everything that was produced since they were last here.

Output a single message in this format:

```
☕ Morning Brief — [date]

📅 Today
- [meeting — time + person + 1-line prep cue]
- ([nothing scheduled] if quiet)

✅ Top 5 from the task list
1. ...
2. ...

📥 Inbox check
- [any inbound replies overnight needing a response]
- [N drafts sitting in your outbox waiting to fire]

🎙 Transcripts to file
- [meeting from yesterday awaiting filing]

📨 Extraction queue ([n] items)
- [queued transcript/research → proposed actions/CRM/decisions]

🖥 Since you were away (what the always-on machine produced)
- [new Cabinet action slate awaiting approve/kill, if any]
- [open sync questions to answer]
- [fresh digests in _routines/runs/ since the last brief — one line each]

⚡ The one thing
[the single highest-leverage action today — drawn from OKRS.md (which goal needs the first move) + the latest Heartbeat]
```

## Process the extraction queue
- Read the extraction queue (e.g. `_memory/extraction-queue.log`). For each unprocessed item, **run it through `INGESTION_GATE.md` first** — tier it 🟢 fact / 🟡 validate / 🔴 disregard.
- Only 🟢 facts (first-party, verifiable) become proposed canonical updates, *with provenance* `(source, as-of date)`. 🟡 (anything flattering, investor-sourced numbers, hearsay) is parked `[unverified]` for the next sync. 🔴 is dropped or filed as positioning only.
- **Apply internal-state mutations** (CRM timestamps, task creation, scorecard touches) and commit `os/auto:`. **Outbound stays draft — you fire send.** Adding a *new person* to the CRM stays a proposal.
- After processing, clear handled lines from the queue so they don't re-surface.

## Rules
- **≤200 words.** It's a cockpit, not a report. If it's longer, it's failing.
- **Never outbound, never money.** Everything is a draft or a proposal until you act.
- Frame "the one thing" against the goals — not the loudest item, the highest-leverage one.
