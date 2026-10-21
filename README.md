# System Design Reference + Personal / Physical AI Lab

This repository contains two major engineering references:

1. **System Design Knowledge Base** — A structured plan and (to be generated) reference library of 300 critical system design questions, architecture diagrams, and engineering trade-offs. See `docs/00_system_design_master_prompt.md`.

2. **Personal AI + Physical AI Lab Architecture** — A proposed local-first architecture for personal cloud, safe AI agents, multi-device sensor streaming, 3D reconstruction / body scanning, and related services. See `docs/01_personal_ai_physical_ai_lab_architecture.md`.

## Status

- Stage 1 of the system design reference is starting: project structure, question index, and diagram inventory will be generated next.
- The Physical AI Lab architecture is a proposal (v0.1). Hardware inventory and current repo state must be re-validated before implementation.

## Structure

```
docs/
  00_system_design_master_prompt.md     # The master generation prompt
  01_personal_ai_physical_ai_lab_architecture.md
  system-design/                        # (to be populated)
    00_README.md
    01_MASTER_KNOWLEDGE_MAP.md
    02_MASTER_QUESTION_INDEX.md
    ...
```

## How to use

- For the system design library: follow the stages in the master prompt, generating content in batches and committing it here.
- For the lab: use the phased plan in the architecture document. Start with Phase 0 (read-only inventory).

