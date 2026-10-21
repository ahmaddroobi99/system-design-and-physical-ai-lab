# System Design Reference + Physical-AI Lab

Engineering references for system design interview prep and a local-first Physical-AI Lab.

**Repository:** https://github.com/ahmaddroobi99/system-design-and-physical-ai-lab

## Contents

| Document | Purpose | Status |
|----------|---------|--------|
| [docs/00_system_design_master_prompt.md](docs/00_system_design_master_prompt.md) | Master prompt to generate a long-lived system design knowledge base (exactly 300 questions, architecture diagrams, trade-offs, case studies). | Prompt ready. STAGE 1 (index + diagram catalog) not yet generated. |
| [docs/01_personal_ai_physical_ai_lab_architecture.md](docs/01_personal_ai_physical_ai_lab_architecture.md) | Whole-lab architecture proposal: personal cloud, safe AI agents, multi-device sensor streaming, 3D/body scanning, search, and operations. | Architecture proposal v0.1. |
| [docs/02_physical-ai-lab-system-design.md](docs/02_physical-ai-lab-system-design.md) | Top-down system design (L0–L3) for the four concrete systems: Personal cloud, Forma (body scan → fit), Guarded agent ops, and Real-time multi-device sensor platform. Includes the predict→update generalization and measurement-first update steps. | Draft v1 (2026-10-20). |

## How to use

### System Design Reference
Follow the stages in `00_system_design_master_prompt.md`:
1. Generate the master question index (all 300 titles + difficulty + diagram IDs).
2. Generate the architecture diagram catalog.
3. Answer questions in batches of 30–60, preserving stable IDs.
4. Commit each stage so the reference stays searchable and versioned.

### Physical-AI Lab
Start with the top-down design in `02_physical-ai-lab-system-design.md` (especially the build order in section 7 and the update-step metrics). Cross-reference the broader architecture and service map in `01_personal_ai_physical_ai_lab_architecture.md`.

**Key principle from both lab docs:** generation is nearly free; verification costs what it always did. Write the measurement before generating the next feature.

## Build order (from the system design doc)

```
C  Guarded agent ops          → gates every later agent change
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

## Next steps

- [ ] Generate STAGE 1 of the system design reference (master index + diagram inventory) and commit it under `docs/system-design/`.
- [ ] Phase 0 inventory of the actual lab hardware and existing Physical AI Lab code.
- [ ] Implement System C P0 (constraint file + disk-identity rule + deny-list) before further agent-driven changes.
- [ ] First restore drill for personal cloud backups.

