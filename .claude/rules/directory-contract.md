# Directory Contract — Mega Brain

> **Versão:** 2.0.0
> **Source of Truth:** `core/paths.py`
> **Enforcement:** `.claude/hooks/directory_contract_guard.py` (PreToolUse, WARN)
> **Keywords:** "directory", "output", "path", "onde salvar", "where to save", "bucket"

---

## Arquitetura Tridimensional (3 Buckets)

```
knowledge/
├── external/       ← Bucket 1: Expert Knowledge (L2)
│   ├── dna/            → DNA schemas per person
│   ├── dossiers/       → Person + theme dossiers
│   ├── playbooks/      → Actionable playbooks
│   ├── sources/        → Source compilations
│   └── inbox/          → Raw expert materials
└── personal/       ← Bucket 3: Cognitive/Private (L3 ONLY)
    ├── _email/         → Email digests
    ├── _messages/      → WhatsApp/Slack
    ├── _calls/         → Call transcripts
    ├── _cognitive/     → Mental models, reflections
    └── inbox/          → Raw personal materials

workspace/              ← Bucket 2: Business Data (ROOT level, L1 template / L2 populated)
├── _org/               → Organization structure
├── _team/              → Team data
├── _finance/           → Financial data
├── _meetings/          → Meeting notes
├── _automations/       → Tool configs
├── _tools/             → Detected tools log
└── inbox/              → Raw business materials
```

## Diretórios e Propósito

| Diretório | Categoria | O Que Pertence | Git |
|-----------|-----------|----------------|-----|
| `core/` | Engine | tasks, workflows, intelligence, paths.py | Tracked |
| `agents/` | Knowledge Agents | conclave, cargo, minds | Tracked |
| `reference/` | Documentation | guides, protocols, templates | Tracked |
| `bin/` | CLI Tools | npm executables | Tracked |
| `system/` | System Config | JARVIS state, DNA, soul | Tracked |
| `.planning/` | GSD Plans | phases, roadmap, state | Tracked |
| `.claude/` | Config + Runtime | hooks, skills, commands, rules | Tracked |
| `artifacts/` | Generated Output | audit reports, validation | Gitignored |
| `logs/` | Session Logs | batches, JSONL audit trails | Gitignored |
| `inbox/` | Raw Materials | L3 personal content | Gitignored |
| `workspace/` | Bucket 2 | Business data, org, finance | Tracked (L1 template, L2 populated) |
| `knowledge/external/` | Bucket 1 | Expert dna, dossiers, playbooks | Tracked (L2) |
| `knowledge/personal/` | Bucket 3 | Cognitive, email, calls | Gitignored (L3) |
| `research/` | Ad-hoc Analysis | L3 blueprints, deep-dives | Gitignored |
| `processing/` | Pipeline Artifacts | speakers, entities, diarization | Gitignored |
| `.data/` | Indexes | RAG, knowledge graph, embeddings | Gitignored |

## Output Routing (quem escreve onde)

| Script/Hook | Escreve Em | Constante em paths.py |
|-------------|------------|----------------------|
| `audit_layers.py` | `artifacts/audit/` | `ROUTING["audit_report"]` |
| `validate_layers.py` | `artifacts/audit/` | `ROUTING["audit_report"]` |
| `session_autosave_v2.py` | `.claude/sessions/` | `ROUTING["session_log"]` |
| `skill_indexer.py` | `.claude/mission-control/` | `ROUTING["skill_index"]` |
| `post_batch_cascading.py` | `logs/batches/` | `ROUTING["batch_log"]` |
| `stop_hook_completeness.py` | `logs/handoffs/` | `ROUTING["handoff"]` |
| `chunker.py` | `.data/rag_expert/` | `ROUTING["rag_chunks"]` |
| `graph_builder.py` | `.data/knowledge_graph/` | `ROUTING["graph"]` |
| `memory_splitter.py` | `knowledge/external/dna/persons/` | `ROUTING["memory_split"]` |
| `nav_map_builder.py` | `knowledge/external/` | `ROUTING["nav_map"]` |
| `sow_generator.py` | `agents/sua-empresa/sow/` | `ROUTING["sow_output"]` |
| `organized_downloader.py` | `inbox/` | `ROUTING["download"]` |
| *(workspace scripts)* | `workspace/` | `ROUTING["workspace_data"]` |
| *(personal scripts)* | `knowledge/personal/` | `ROUTING["personal_data"]` |

## RAG Isolation

| Bucket | RAG Index | Constante |
|--------|-----------|-----------|
| External (experts) | `.data/rag_expert/` | `RAG_EXPERT` |
| Workspace (business) | `.data/rag_business/` | `RAG_BUSINESS` |
| Personal (cognitive) | `knowledge/personal/index/` | via `KNOWLEDGE_PERSONAL` |

## Proibições

- **`docs/`** — PROIBIDO para novos arquivos. Usar `reference/` em vez disso.
- **`knowledge/` root** — PROIBIDO. Conteúdo vai em `external/`, `workspace/`, ou `personal/`.
- **Novos top-level dirs** — Não criar diretórios na raiz sem atualizar este contrato.
- **Hardcoded paths** — Novos scripts DEVEM importar de `core/paths.py`.
- **L3 leaks** — NUNCA expor dados de `knowledge/personal/` em L1/L2.

## Como Usar

```python
from core.paths import ROUTING, KNOWLEDGE_EXTERNAL, KNOWLEDGE_WORKSPACE, KNOWLEDGE_PERSONAL

# Correto: usar constante
output = ROUTING["audit_report"] / "report.json"
dna_path = KNOWLEDGE_EXTERNAL / "dna" / "persons" / "alex-hormozi"
workspace = ROUTING["workspace_data"] / "_meetings"  # resolves to workspace/_meetings

# Errado: hardcodar path
output = Path("knowledge/dna/persons/alex-hormozi")  # PROIBIDO (stale path)
```
