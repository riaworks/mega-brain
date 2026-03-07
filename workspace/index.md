# Knowledge / Workspace

> **Bucket 2** -- Business context and operational data.
> **Layer:** L2 (Pro, tracked scaffolding) / L3 (populated content gitignored)
> **paths.py constant:** `KNOWLEDGE_WORKSPACE`

## Purpose

This bucket contains **business-specific** knowledge: team structure, financial data,
meeting notes, tool configurations, and automation workflows. It provides the real-world
context that transforms generic expert knowledge into actionable recommendations.

## Structure

```
knowledge/workspace/
  _org/             -- Organization charts, role definitions, SOWs
  _team/            -- Team profiles, performance data, hiring pipeline
  _finance/         -- Financial data, KPIs, DRE, unit economics
  _meetings/        -- Meeting notes, decisions, action items
  _tools/           -- Tool configurations, CRM setup, integrations
  _automations/     -- n8n workflows, Zapier configs, automation docs
  inbox/            -- Triage area for new business content
    pending/        -- Awaiting classification
    rejected/       -- Did not pass quality gate
```

## Key Files

| File | Purpose |
|------|---------|
| `MASTER-INDEX.md` | Human-readable index of all workspace content |
| `MISSING-CONTEXT-LOG.md` | Tracks business context gaps detected by agents |
| `DETECTED-TOOLS-LOG.md` | Tools and platforms detected during sessions |
| `SETUP-PENDING.md` | Pending setup items for workspace integrations |

## Routing

```python
from core.paths import KNOWLEDGE_WORKSPACE, ROUTING

ROUTING["workspace_data"]   # -> knowledge/workspace/
ROUTING["workspace_inbox"]  # -> knowledge/workspace/inbox/
ROUTING["rag_business"]     # -> .data/rag_business/ (index built from this bucket)
```

## Integration Points

- Agents consult workspace/ before making strategic recommendations (Rule #16)
- The `context_assembler.py` pulls from workspace/ for business-aware RAG
- MCP servers (ClickUp, Notion) can push data into workspace/inbox/
- Financial data here feeds the CFO agent's MEMORY.md

## Security

Populated content in this bucket is L3 (gitignored). Only the directory scaffolding
and template files (.gitkeep, index.md) are tracked. Never commit actual business
data, financial figures, or team personal information.
