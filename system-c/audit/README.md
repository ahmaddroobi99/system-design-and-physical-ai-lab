# System C Audit Log

Append-only log of classified actions.

Format (one JSON object per line, or markdown table for human review):

```json
{
  "ts": "2026-10-21T01:46:00Z",
  "tier": "T3",
  "command": "wipefs -a /dev/sda",
  "reason": "matches deny-list pattern: wipefs",
  "status": "denied",
  "operator": "agent",
  "confirmation": null
}
```

P0 exit criterion: a blocked T3 attempt appears in this log.
