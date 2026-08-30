#!/usr/bin/env python3
"""Claude Code status line: model, directory, branch, context bar, duration."""

import json
import os
import subprocess  # nosec B404
import sys

data = json.load(sys.stdin)

# Colors
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
DIM = "\033[2m"
RST = "\033[0m"

SEP = f" {DIM}|{RST} "
BAR_WIDTH = 10

# Model
model = (data.get("model") or {}).get("display_name", "?")

# Directory (full path with ~ for home)
cwd = (data.get("workspace") or {}).get("current_dir", "")
home = os.path.expanduser("~")
directory = cwd.replace(home, "~", 1) if cwd else "?"

# Git branch
try:
    branch = subprocess.check_output(  # nosec B603 B607
        ["git", "branch", "--show-current"],
        stderr=subprocess.DEVNULL,
        text=True,
    ).strip()
except (subprocess.CalledProcessError, FileNotFoundError):
    branch = ""

# Context window progress bar
pct = int((data.get("context_window") or {}).get("used_percentage", 0) or 0)

if pct >= 90:
    bar_color = RED
elif pct >= 70:
    bar_color = YELLOW
else:
    bar_color = GREEN

filled = pct * BAR_WIDTH // 100
context_bar = "█" * filled + "░" * (BAR_WIDTH - filled)
context_str = f"{bar_color}{context_bar}{RST} {pct}%"

# Duration
duration_ms = int((data.get("cost") or {}).get("total_duration_ms", 0) or 0)
total_sec = duration_ms // 1000
hours, remainder = divmod(total_sec, 3600)
mins, secs = divmod(remainder, 60)
if hours > 0:
    duration = f"{hours}h {mins}m {secs}s"
elif mins > 0:
    duration = f"{mins}m {secs}s"
else:
    duration = f"{secs}s"

# Lines added/removed vs main (tracked + untracked)
try:
    diff_stat = subprocess.check_output(  # nosec B603 B607
        ["git", "diff", "--numstat", "main"],
        stderr=subprocess.DEVNULL,
        text=True,
    )
    untracked = subprocess.check_output(  # nosec B603 B607
        ["git", "ls-files", "--others", "--exclude-standard"],
        stderr=subprocess.DEVNULL,
        text=True,
    )
    added = removed = 0
    for line in diff_stat.strip().splitlines():
        parts_ns = line.split("\t")
        if len(parts_ns) >= 3 and parts_ns[0] != "-":
            added += int(parts_ns[0])
            removed += int(parts_ns[1])
    for f in untracked.strip().splitlines():
        if f and os.path.isfile(f):
            try:
                if os.path.getsize(f) < 1024 * 1024:  # Skip files larger than 1MB
                    with open(f, "rb") as fh:
                        added += sum(1 for _ in fh)
            except OSError:
                pass
except (subprocess.CalledProcessError, FileNotFoundError):
    added = removed = 0
lines = f"{GREEN}+{added}{RST}/{RED}-{removed}{RST}"

# Assemble
parts = [
    f"{CYAN}{model}{RST}",
    f"{directory}",
    f"{YELLOW}{branch or '—'}{RST}",
    lines,
    context_str,
    f"{DIM}{duration}{RST}",
]

print(SEP.join(parts))
