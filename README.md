# System Design Reference + Physical-AI Lab

Engineering references for system design interview prep and a local-first Physical-AI Lab.

**Repository:** https://github.com/ahmaddroobi99/system-design-and-physical-ai-lab

## Contents

| Document / path | Purpose | Status |
|-----------------|---------|--------|
| [docs/00_system_design_master_prompt.md](docs/00_system_design_master_prompt.md) | Master prompt to generate a long-lived system design knowledge base (exactly 300 questions, architecture diagrams, trade-offs, case studies). | Prompt ready. STAGE 1 not yet generated. |
| [docs/01_personal_ai_physical_ai_lab_architecture.md](docs/01_personal_ai_physical_ai_lab_architecture.md) | Whole-lab architecture proposal: personal cloud, safe AI agents, multi-device sensor streaming, 3D/body scanning, search, and operations. | Architecture proposal v0.1. |
| [docs/02_physical-ai-lab-system-design.md](docs/02_physical-ai-lab-system-design.md) | Top-down system design (L0–L3) for Systems A–D: Personal cloud, Forma, Guarded agent ops, Real-time sensor platform. | Draft v1 (2026-10-20). |
| [system-c/](system-c/) | **System C — Guarded Agent Ops** (Linux architect agent). Phase P0: constraints, disk-identity rule, deny-list, minimal classifier. | **P0 started.** |

## System C — Guarded Agent Ops (started)

Phase P0 artifacts are in `system-c/`:

- `CONSTRAINTS.md` — hard rules, action tiers (T0–T3), disk-identity rule
- `policy/deny-list.txt` — patterns that force T3
- `policy/classify.py` — minimal classifier (does not execute)
- `audit/` — append-only log location

**P0 exit criterion:** a blocked T3 attempt shows up in the audit log.

```bash
python3 system-c/policy/classify.py "wipefs -a /dev/sda"
# → T3, exit 2
```

## How to use the other references

### System Design Reference
Follow the stages in `00_system_design_master_prompt.md`:
1. Generate the master question index (all 300 titles + difficulty + diagram IDs).
2. Generate the architecture diagram catalog.
3. Answer questions in batches of 30–60, preserving stable IDs.

### Physical-AI Lab
Start with the top-down design in `02_physical-ai-lab-system-design.md` (especially section 7 build order and the update-step metrics). Cross-reference the broader architecture in `01_personal_ai_physical_ai_lab_architecture.md`.

**Key principle:** generation is nearly free; verification costs what it always did. Write the measurement before generating the next feature.

## Build order (from the system design doc)

```
C  Guarded agent ops          → gates every later agent change   ← STARTED (P0)
   ↓
A-P0  Platform + backups      → restore must pass before new data is stored
   ↓
├── D-P0/P1  Sensor platform  → measure latency and clock error early
├── B-P0     Forma measurement → 10 people, one error report
└── A-P1+    Rest of personal cloud
```

## Principles

- Local-first. Remote access only via overlay VPN.
- One SSO in front of every UI.
- All agent-made changes go through guarded ops (System C).
- Raw personal data never leaves the lab unencrypted.
- Numbers marked *target* are hypotheses until measured.
- Tech choices live at L2 so they can be swapped without rewriting L0–L1.
- Never address disks by transient `/dev/sdX` or `/dev/nvmeXnY`. Use serial or UUID.

## Next steps

- [ ] Wire System C classifier into an agent harness / pre-execution hook and record a blocked T3 in `system-c/audit/`.
- [ ] System C P1: snapshot service + verifier + rollback drill on external HDD.
- [ ] Generate STAGE 1 of the system design reference under `docs/system-design/`.
- [ ] Phase 0 inventory of actual lab hardware and existing Physical AI Lab code.
- [ ] First restore drill for personal cloud backups.

