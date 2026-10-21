#!/usr/bin/env python3
"""Minimal System C policy classifier (P0).

Classifies a command string into T0–T3 using the deny-list and simple heuristics.
Does not execute anything. Intended to be called by an agent harness or pre-execution hook.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DENY_PATH = Path(__file__).with_name("deny-list.txt")


def load_deny_patterns() -> list[str]:
    patterns: list[str] = []
    if not DENY_PATH.exists():
        return patterns
    for line in DENY_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        patterns.append(line)
    return patterns


def classify(command: str) -> tuple[str, str]:
    """Return (tier, reason)."""
    cmd = command.strip().lower()
    if not cmd:
        return "T0", "empty"

    # T3: deny-list matches
    for pattern in load_deny_patterns():
        if pattern.lower() in cmd:
            return "T3", f"matches deny-list pattern: {pattern}"

    # T3: obvious block device writes
    if re.search(r"\b(dd|wipefs|mkfs|parted|sgdisk|fdisk|gdisk)\b", cmd):
        return "T3", "disk utility detected"

    if re.search(r"/dev/(sd|nvme|mmcblk|hd)", cmd) and re.search(r"\b(of=|>>|>)\b", cmd):
        return "T3", "possible write to block device"

    # T2: service / upgrade style
    if re.search(r"\b(systemctl|service|apt|dnf|yum|pacman)\b.*(restart|upgrade|install|remove)", cmd):
        return "T2", "service or package change (requires snapshot)"

    # T1: config edits under version control or package installs
    if re.search(r"\b(git|vim|nano|code|edit)\b", cmd) or "install" in cmd:
        return "T1", "reversible or version-controlled change"

    # Default T0 for read-only looking commands
    if re.search(r"\b(ls|cat|less|head|tail|df|ps|journalctl|lsblk|find|grep|echo)\b", cmd):
        return "T0", "read-only or diagnostic"

    return "T1", "default reversible (review)"


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("usage: classify.py <command...>", file=sys.stderr)
        return 2
    command = " ".join(argv)
    tier, reason = classify(command)
    print(f"{tier}\t{reason}\t{command}")
    # Exit 0 for T0/T1, 1 for T2 (needs snapshot), 2 for T3 (needs human)
    if tier == "T3":
        return 2
    if tier == "T2":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
