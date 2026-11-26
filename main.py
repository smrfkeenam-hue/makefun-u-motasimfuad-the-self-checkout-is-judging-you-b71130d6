import os

ENTRY = "Unexpected item in the bagging area: your dignity. It has been here since the instant noodles. Please remove both."
# One line, 114 characters, no trailing newline. Machine voice: the classic
# "unexpected item" error turned into a judgement of the shopper — the noodles
# are the evidence of how long the dignity has been missing, and the machine
# treats dignity and noodles as equally disposable: "Please remove both."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# Write exactly the entry text, no trailing newline, so the file is the line.
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
