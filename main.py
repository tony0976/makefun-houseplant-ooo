"""Writes a houseplant's out-of-office auto-reply to /output/entry.txt."""
import os

TEXT = "I'm out of office. The cactus is watering itself now, and frankly, it was doing a better job than you."

# Rule: the auto-reply must be a single line of 1 to 120 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 120, f"entry must be one line, 1-120 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
