# The ingestion gate — what's allowed into the brain

> **In one line:** check what you feed the AI before it believes it — especially numbers that flatter you.

> **A bad input doesn't sit there quietly — an AI repeats it back to you with total confidence.** So every new input — a transcript, an email, a number, a claim — is tiered *before* it's allowed to write to a canonical file. Nothing that flatters you enters as fact unchecked.
>
> New transcripts and research get queued (e.g. to `_memory/extraction-queue.log`). Whichever routine consumes that queue — the morning brief, a transcript sweep, your chief-of-staff pass — **must run this gate on each item** before proposing any change to the CRM, the decisions log, or the scorecard.

**Last updated:** [date] · Pairs with `SOURCES_OF_TRUTH.md` (the precedence ladder).

---

## The three tiers — stack-rank every input

| Tier | What it is | What happens |
|---|---|---|
| 🟢 **FACT** | First-party, verifiable: signed docs; what a **customer/counterparty said about their own situation**; data you can see; a decision you confirmed. | May enter canonical files directly — **with provenance** (see below). |
| 🟡 **VALIDATE** | Second-hand, opinion, or flattering: advisor/connector hearsay; anything that rounds in your favour (revenue, traction, growth, committed $, valuation, audience size); **numbers said to investors, customers, partners, or your audience**; a claim with no source. | **Does not enter as fact.** Park it, tag `[unverified]`, and surface to you (or check against a tier-1/2 source) before it's promoted. |
| 🔴 **DISREGARD** | Positioning, speculation, rumour, vibes; aspiration stated as if real. | Never enters the brain as fact. Note it as positioning if useful (e.g. in a deck file), never in a truth file. |

---

## The rules that earn their keep

1. **What a counterparty says about their own situation is fact. What you say to win the room is positioning.** Numbers said to investors, customers, partners, or your audience are goals and framing — they must never leak back into "what's actually true" (investors are just the most common example). You pitch the ambition; you've *closed* the fact. Different columns, always.
2. **A flattering number is guilty until validated.** Any figure that helps your story gets a tier-1/2 check before it's promoted from 🟡 to 🟢.
3. **Speaker incentive is part of the tier.** Ask of every source: what are they selling, whose book are they talking? A glowing claim from someone who profits from your optimism is 🟡 by default.
4. **A file can be fresh and wrong.** Recency is not truth. Provenance + validation is.

---

## Tier is "is it true?" — weight is "how much does it matter?"

A fact can still be trivial; a true thing from the wrong mouth can still mislead. So after you tier an input for *truth*, weight it for *attention* — and this is a judgment call the OS surfaces to **you**, it never decides alone. Three questions set the weight:

- **Whose book?** Discount anyone talking their own interest — an advisor selling a service, an investor managing you, a vendor pitching. A glowing claim from someone who profits from your optimism is low-weight by default.
- **Does it touch a goal?** If it doesn't move one of your objectives, it's a footnote, not a headline. Capture it; don't act on it.
- **One-off or pattern?** A single offhand remark is weak signal. The *same* thing from three sources — or twice from the same person — is a pattern. Weight it up.

**Transcripts come in whole; they don't come in equal.** Capture every meeting (drop the transcript in, or connect your notes tool) — but a transcript is a *source, not a verdict*. The OS reads it, proposes what's fact and how much it matters, and **asks you to confirm relevance and weight before anything is lodged.** You're the one who knows the throwaway line was actually the most important thing said.

---

## Provenance — every fact carries its origin

When a fact enters a canonical file, stamp it: **source + as-of date.** e.g. `(per the customer call, 12 May)` or `(their email, 12 May)`. This is what lets the conflict audit tell a stale fact from a current one — it reads the date *inside* the line, not the file's timestamp. A line without provenance is a line you can't trust later.

---

## At the gate, the consumer does:

1. **Tier** each queued item (🟢 / 🟡 / 🔴).
2. For 🟢 → propose the canonical update **with provenance**.
3. For 🟡 → park as `[unverified]` and add to the next sync's "confirm these" list.
4. For 🔴 → drop, or file as positioning only — never in a truth file.
5. **Never promote a number that flatters** without a tier-1/2 check.

The gate is dull and it's the most valuable thing here. Everything downstream — the dashboard, the routines, the AI's advice — is only as good as what this gate let through.
