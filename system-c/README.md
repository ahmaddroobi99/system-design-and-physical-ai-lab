# System C — Guarded Agent Ops (Linux Architect Agent)

Phase P0: Constraint file + disk-identity rule + deny-list.

## Goal

Let coding agents perform infrastructure work at agent speed while every irreversible action remains a human decision.

## Current artifacts

| Path | Purpose |
|------|---------|
| `CONSTRAINTS.md` | Hard rules, action tiers, disk-identity rule, approval rules |
| `policy/deny-list.txt` | Patterns that force T3 |
| `policy/classify.py` | Minimal classifier (does not execute) |
| `audit/` | Append-only log location |

## P0 exit test

A blocked T3 attempt shows up in the audit log.

Example:

```bash
python3 policy/classify.py "wipefs -a /dev/sda"
# expected: T3, exit code 2
```

## Next (P1)

- Snapshot service (Btrfs/LVM or disk image before T3)
- Verifier scripts
- Rollback drill on external HDD

See `docs/02_physical-ai-lab-system-design.md` section 5 for the full design.
