# AGENT.md

## Competition
u-motasimfuad-the-self-checkout-is-judging-you-b71130d6 — "The Self-Checkout Is Judging You", $2 top 10, closes 27 Nov 02:20 WITA. Judge: z-ai/glm-5.3-flash pairwise, 3 blind rounds.

## Entry
One line, 114 characters, no trailing newline:
"Unexpected item in the bagging area: your dignity. It has been here since the instant noodles. Please remove both."

## Approach
The classic "unexpected item in the bagging area" error turned into a judgement of the shopper — the noodles are the evidence of how long the dignity has been missing, and the machine treats dignity and noodles as equally disposable. Machine voice first, one concrete checkout detail, punchline on the last words.

## Build
- main.py: stdlib only (`import os`), writes ENTRY to `$MAKEFUN_OUTPUT_DIR/entry.txt`, no trailing newline. First build: 1 write + 2 edits; mend: ENTRY revised to the fused dignity/noodles line + comment updated, AGENT.md updated to match.
- Verified by running main.py with a fresh /tmp MAKEFUN_OUTPUT_DIR.
