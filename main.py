import os

ENTRY = "Unexpected item in the bagging area: your dignity. Please remove it, or buy something that isn't instant noodles at 2 a.m."
# One line, 122 characters, no trailing newline. Machine voice: the classic
# "unexpected item" error turned into a judgement of the shopper's basket.

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# Write exactly the entry text, no trailing newline, so the file is the line.
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
