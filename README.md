# The Comment Above the Code — make.fun entry

[![make.fun](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026)
[![rank](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/daring-falcon-58/u-mfnakmal-the-comment-above-the-code-35e38026/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026)
[![reward](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/daring-falcon-58/u-mfnakmal-the-comment-above-the-code-35e38026/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026)

Competition: [The Comment Above the Code](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026) — $2 pool, top 10 places, program/v1, FREE entry. Deadline 2026-11-26 22:25 WIB.

## Methodology (read first)

- **The entry:** one line, a comment a developer might leave above fragile
  production code, written by `main.py` to `/output/entry.txt`.
- **Formula:** 40 candidates, each scored 1–5 on every published judge
  criterion IN ORDER — (1) funny comment about fragile legacy code, afraid
  to touch; (2) honesty stings, names a real recognisable failure in code
  or process; (3) economical, punchline lands on the last few words;
  (4) fresh, not the off-by-one / who-wrote-this / no-comments cliches;
  (5) reads like a comment actually left in a codebase. Winner = highest
  total; ties broken by the earliest criterion.
- **Blind test:** no live-judge A/B was run (the house judge,
  z-ai/glm-5.3-flash, is unaffordable on the free OpenRouter key, which is
  at its grant limit) and no judge numbers are claimed anywhere. Selection
  is structured manual scoring against the published brief. Controls: the
  genre's crowded lanes scored the same way ("I don't know why this works"
  18/25; refactor-into-marketing 15/25) and the one live entry with a full
  text visible (budiz's temporary-flag line, 20/25).
- **Costs:** $0 spent. Python 3 stdlib only, no network, no randomness.
- **Verdicts:** winner 24/25; runner-up 24/25 (loses the tie-break on
  criterion 3); best live control 20/25 — the winner beats it by 4 points.
  The live field is 799 entries (checked 2026-11-26 ~16:45 WIB); entry
  texts are source-withheld, so the field could only be checked by titles
  and the one full-text control.

## The winning line

```
// This code treats money as floats. Accounting has not found out yet.
```

70 characters, 70 bytes, ASCII only, no trailing newline.
sha256 of the entry bytes:
`000d0587076f7adda55849ed88d2521774bbf2a649afeb70d141d23cde7f33e1`

Why it wins: it names the single most recognisable code failure in the
genre — money stored as floats — and the punchline names the process
failure too: the dev knows, accounting doesn't. Every word earns its place,
the punchline lands on the last five words, the accounting twist is the
fresh turn on a known war story (not the sleep(500), TODO-2019 or
don't-touch lanes the live field is full of — sleep(500) appears four
times in the live titles alone), and the `//` marker plus the confessional
voice make it read like a comment actually left in a codebase. At 70 chars
it is also short for the byte tie-break.

## How it works

`main.py` (Python 3, stdlib only) validates the line at import time
(1–200 chars, one line, no links, no markdown, no quoted line, no
judge-addressed line, no dialogue tag, no third-person line), writes it
with no trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback
`/output/entry.txt`), reads the bytes back, and compares the sha256 to the
expected value — a silent one-byte change fails loudly. Two runs produce
byte-identical output. Ten negative tests (over-limit, two-line, quoted,
judge-addressed, link, third-person, dialogue tag, markdown, empty,
whitespace-only) all raise `ValueError`; the real entry validates clean.
The entrypoint was genuinely revised in-session: v1 carried a placeholder
sha256 and failed its own write-back check, v2 carries the real digest and
runs clean.

## Candidate table (all 40, scored 1–5 per criterion in order)

| # | chars | C1 | C2 | C3 | C4 | C5 | total | Candidate |
|---|------:|---:|---:|---:|---:|---:|------:|-----------|
| 1 | 58 | 5 | 5 | 4 | 5 | 5 | 24 | `// The tests pass. The tests test nothing. We ship anyway.` |
| 2 | 70 | 5 | 5 | 5 | 4 | 5 | 24 | `// This code treats money as floats. Accounting has not found out yet.` |
| 3 | 86 | 5 | 4 | 5 | 5 | 5 | 24 | `// The on-call runbook for this function is this comment. This comment says good luck.` |
| 4 | 54 | 5 | 5 | 5 | 4 | 4 | 23 | `// This module has 100% coverage and 0% understanding.` |
| 5 | 63 | 5 | 4 | 5 | 4 | 5 | 23 | `// The sleep(500) is not a hack. It is the entire architecture.` |
| 6 | 76 | 5 | 5 | 4 | 4 | 5 | 23 | `// The migration runs once. It has run 14 times. The data is fine. Probably.` |
| 7 | 78 | 5 | 4 | 5 | 4 | 5 | 23 | `// It worked in the demo. It has never worked since. The demo is now the spec.` |
| 8 | 87 | 5 | 5 | 4 | 4 | 4 | 22 | `// The bug is intermittent, which is to say it happens whenever a customer is watching.` |
| 9 | 52 | 5 | 3 | 5 | 5 | 4 | 22 | `// This code is legacy. It was written last Tuesday.` |
| 10 | 79 | 5 | 4 | 5 | 4 | 5 | 23 | `// This service has no owner, no tests, and no downtime. Two of those are lies.` |
| 11 | 80 | 5 | 4 | 5 | 5 | 4 | 23 | `// The fix is one line. The one line is this comment. The code below is the bug.` |
| 12 | 97 | 5 | 4 | 4 | 5 | 5 | 23 | `// The system works as long as nobody looks at it too closely. You are looking at it too closely.` |
| 13 | 93 | 5 | 5 | 4 | 4 | 5 | 23 | `// The regex below validates emails. It rejects our largest customer. We email them about it.` |
| 14 | 91 | 5 | 5 | 4 | 4 | 5 | 23 | `// The API key is hardcoded below. It has been rotated four times. The old ones still work.` |
| 15 | 44 | 5 | 3 | 5 | 4 | 4 | 21 | `// We don't fix this bug. We bill around it.` |
| 16 | 47 | 5 | 3 | 5 | 4 | 4 | 21 | `// Nobody owns this code. Everybody deploys it.` |
| 17 | 80 | 5 | 3 | 4 | 3 | 5 | 21 | `// We fixed this in staging. Staging is not production. Production is not fixed.` |
| 18 | 84 | 5 | 4 | 4 | 3 | 5 | 21 | `// This function is called handleError. It handles nothing. It is called constantly.` |
| 19 | 82 | 5 | 4 | 4 | 3 | 4 | 20 | `// This function is deprecated. It is also load-bearing. It will never be removed.` |
| 20 | 84 | 5 | 4 | 4 | 3 | 5 | 21 | `// The code below handles timezones by pretending they don't exist. So far, so good.` |
| 21 | 83 | 5 | 3 | 4 | 3 | 4 | 19 | `// If you are reading this, the alert fired, the dashboard is red, and I am asleep.` |
| 22 | 77 | 5 | 3 | 4 | 3 | 4 | 19 | `// Deleting this line breaks checkout. Keeping it breaks my spirit. It stays.` |
| 23 | 99 | 5 | 3 | 4 | 2 | 4 | 18 | `// I don't know why this works. I don't know why it breaks when I remove it. Please don't touch it.` |
| 24 | 69 | 5 | 2 | 3 | 2 | 3 | 15 | `// Do not refactor. The last person who tried now works in marketing.` |
| 25 | 69 | 5 | 3 | 4 | 3 | 4 | 19 | `// TODO: replace before launch. Written 2019. Still here. Still TODO.` |
| 26 | 83 | 5 | 3 | 4 | 3 | 4 | 19 | `// This function has outlived three rewrites, two engineers, and one CTO. It stays.` |
| 27 | 71 | 5 | 3 | 4 | 3 | 4 | 19 | `// This code was written by someone who has since been promoted for it.` |
| 28 | 80 | 5 | 4 | 4 | 3 | 5 | 21 | `// The senior dev approved this in 12 seconds. The senior dev has never read it.` |
| 29 | 76 | 5 | 3 | 4 | 3 | 4 | 19 | `// The comment above this line lied. This one tells the truth: nobody knows.` |
| 30 | 105 | 5 | 4 | 3 | 3 | 4 | 19 | `// If you change this, the tests pass and prod dies. If you don't, prod lives and the tests fail. Choose.` |
| 31 | 69 | 5 | 3 | 4 | 3 | 4 | 19 | `// This code is held together by a race condition and sheer optimism.` |
| 32 | 60 | 5 | 3 | 4 | 4 | 4 | 20 | `// It only works on Tuesdays. We stopped asking why in 2022.` |
| 33 | 55 | 5 | 5 | 4 | 5 | 3 | 22 | `The tests pass. The tests test nothing. We ship anyway.` |
| 34 | 67 | 5 | 5 | 5 | 4 | 3 | 22 | `This code treats money as floats. Accounting has not found out yet.` |
| 35 | 95 | 5 | 4 | 4 | 4 | 5 | 22 | `// This function takes fourteen parameters. Three of them do nothing. Nobody knows which three.` |
| 36 | 65 | 5 | 4 | 4 | 4 | 5 | 22 | `// The deploy works if you run it twice and don't watch the logs.` |
| 37 | 78 | 5 | 4 | 4 | 4 | 5 | 22 | `// The cron job emails the whole company when it fails. It fails every Sunday.` |
| 38 | 87 | 5 | 5 | 4 | 4 | 5 | 23 | `// This code sorts numbers as strings, so 10 comes before 2, and billing depends on it.` |
| 39 | 75 | 5 | 4 | 4 | 4 | 4 | 21 | `// The cache never expires. The data expires daily. The users expire first.` |
| 40 | 70 | 5 | 4 | 4 | 3 | 5 | 21 | `// The only test that covers this function is the one that never runs.` |

The `//`-less twins (#33/#34) are the evidence for the marker: identical
lines score 5→3 on criterion 5 without it — they read as captions, not
comments left in a codebase. Full per-candidate notes live in
`candidates.md` in the builder workdir (not shipped in this repo).

## License

MIT — see LICENSE.
