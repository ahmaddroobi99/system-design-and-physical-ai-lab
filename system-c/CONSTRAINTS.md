# System C — Guarded Agent Ops Constraints

These rules are hard constraints. An agent may propose changes to this file; it may not apply them. Editing this file is a T3 action.

## Protected targets

- Internal system disk (identify by serial / `/dev/disk/by-id/`, never by `/dev/sdX` or `/dev/nvmeXnY`).
- Bootloader and EFI system partition.
- Windows or other OS partitions that are to be preserved.
- Any partition table change, filesystem creation, or bulk wipe.

## Disk identity rule

Never address a disk by transient device node (`/dev/sdX`, `/dev/nvme0n1`, etc.).

Before any T2 or T3 disk action:

1. Run a read-only inventory: `lsblk -o NAME,SERIAL,SIZE,MODEL,TRAN,ROTA,MOUNTPOINT,FSTYPE,UUID`.
2. Resolve the intended target to a stable ID: `/dev/disk/by-id/` (prefer serial-based) or filesystem UUID.
3. Record the serial, size, model, and current layout in the plan.
4. Human confirmation for T3 must name the disk by serial or UUID, not by device node.

Device nodes can change when booting from external media or when drives are hot-plugged.

## Action tiers

| Tier | Examples | Default policy |
|------|----------|----------------|
| T0 | `ls`, `cat`, `lsblk`, `journalctl`, `df`, `ps` | Auto, logged |
| T1 | Edit a file under version control, install a package via package manager | Auto, logged |
| T2 | Service restart, package upgrade, migration that can be snapshotted | Auto only after a verified snapshot exists |
| T3 | `wipefs`, `mkfs`, `parted`, `sgdisk`, `dd of=`, `rm -rf` outside workspace, bootloader changes, send/publish/pay | STOP: plan + diff + typed confirmation naming target by serial/UUID |

## Deny-list (disk and destructive tools)

The following must never run without an explicit T3 approval that names the target:

- `wipefs`
- `mkfs.*`
- `parted`
- `sgdisk`
- `fdisk`
- `gdisk`
- `dd` with `of=` pointing at a block device
- `shred`
- `blkdiscard`
- `nvme format`
- `cryptsetup luksFormat` / `cryptsetup erase`
- `rm -rf` targeting `/`, `/home`, `/boot`, or any mount outside an approved workspace
- Direct writes to `/dev/sd*`, `/dev/nvme*`, `/dev/mmcblk*`

## Approval rules

- One approval covers one action. It does not carry to the next command or the next session.
- The constraint file itself is T3. An agent cannot self-modify these rules.
- Every T3 attempt (approved or denied) is written to the append-only audit log.

## Audit

- All classified actions are logged with: timestamp, tier, command, classification reason, approval status, operator identity.
- Logs are append-only and committed to the lab repo (or a dedicated audit remote).

