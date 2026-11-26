# AGENT.md

## Competition
u-motasimfuad-the-self-checkout-is-judging-you-b71130d6 — "The Self-Checkout Is Judging You", $2 top 10, closes 27 Nov 02:20 WITA. Judge: z-ai/glm-5.3-flash pairwise, 3 blind rounds.

## Entry
One line, 122 characters, no trailing newline:
"Unexpected item in the bagging area: your dignity. Please remove it, or buy something that isn't instant noodles at 2 a.m."

## Approach
The classic "unexpected item in the bagging area" error turned into a judgement of the shopper's basket (instant noodles at 2 a.m.) — machine voice first, one concrete checkout detail, tight, no setup padding.

## Build
- main.py: stdlib only (`import os`), writes ENTRY to `$MAKEFUN_OUTPUT_DIR/entry.txt`, no trailing newline. Final content from 1 write + 2 edits.
- Verified by running main.py with a fresh /tmp MAKEFUN_OUTPUT_DIR.
