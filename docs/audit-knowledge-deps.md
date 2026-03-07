# Auditoria de Dependências — knowledge/

> **Data:** 2026-03-05
> **Fase:** 0 — Verificação obrigatória (PRD Megabrain 3D)
> **Status:** COMPLETO

---

## Resumo Executivo

**127+ arquivos** referenciam `knowledge/` em todo o repositório. Severidade: **ALTA** — qualquer reestruturação sem atualizar ponteiros quebra RAG, agentes e pipeline.

---

## 1. Scripts Python (19 arquivos)

### core/intelligence/rag/ (CRÍTICOS)

| Script | Paths Hardcodados | Risco |
|--------|------------------|-------|
| `chunker.py` | `knowledge/dna`, `knowledge/dossiers/persons`, `knowledge/dossiers/themes`, `knowledge/playbooks` | **ALTO** — RAG quebra |
| `graph_builder.py` | `knowledge/dna/persons` | **ALTO** — Graph quebra |
| `hybrid_index.py` | via chunker paths | MÉDIO |
| `hybrid_query.py` | via chunker paths | MÉDIO |
| `mcp_server.py` | via chunker/query | MÉDIO |
| `adaptive_router.py` | via search pipeline | MÉDIO |
| `self_rag.py` | via search pipeline | MÉDIO |

### core/intelligence/ (outros)

| Script | Paths Hardcodados | Risco |
|--------|------------------|-------|
| `context_assembler.py` | `knowledge/dossiers/`, `knowledge/playbooks/` | **ALTO** |
| `query_analyzer.py` | agent-to-domain mapping | MÉDIO |
| `entities/bootstrap_registry.py` | `knowledge/dna/DOMAINS-TAXONOMY.yaml`, `knowledge/dossiers/persons`, `knowledge/dossiers/themes` | **ALTO** |
| `memory_splitter.py` | `knowledge/dna/persons/` | **ALTO** |
| `dossier_tracer.py` | `knowledge/dossiers/` | MÉDIO |
| `nav_map_builder.py` | `knowledge/` (all subdirs) | **ALTO** |
| `validation/audit_layers.py` | via ROUTING (migrated) | BAIXO |
| `validation/validate_layers.py` | via ROUTING (migrated) | BAIXO |

### .claude/hooks/

| Script | Paths Hardcodados | Risco |
|--------|------------------|-------|
| `post_batch_cascading.py` | `knowledge/` (KNOWLEDGE_DIR) | MÉDIO |
| `skill_router.py` | indirect via skill index | BAIXO |

---

## 2. JavaScript (2 arquivos)

| Arquivo | Paths | Risco |
|---------|-------|-------|
| `bin/lib/installer.js` | Scaffolds `knowledge/` subdirs | MÉDIO |
| `bin/utils/pro-detector.js` | Checks populated `knowledge/` | MÉDIO |

---

## 3. Agent DNA-CONFIG.yaml (45+ arquivos)

Todos os cargo agents em `agents/cargo/` possuem DNA-CONFIG.yaml que hardcodam:
- `/knowledge/dna/persons/{PESSOA}/`
- `/knowledge/dna/AGGREGATED/`
- `/knowledge/dossiers/persons/`
- `/knowledge/dossiers/themes/`

**Exemplos:** CLOSER, CFO, CRO, CMO, BDR, SDR-MANAGER, etc.

---

## 4. Markdown Docs (40+ arquivos)

- `CLAUDE.md` (tree diagram references `knowledge/`)
- `.claude/rules/` (multiple rules reference knowledge paths)
- `agents/` AGENT.md files (MAPA DE NAVEGAÇÃO sections)
- `reference/` docs

---

## 5. Configuração

| Arquivo | Referências | Risco |
|---------|------------|-------|
| `core/paths.py` | `KNOWLEDGE = ROOT / "knowledge"`, ROUTING entries | **CENTRAL** — update here first |
| `.gitignore` | Lines 125, 205-210, 452-520 | MÉDIO |
| `package.json` | Lines 135-149 (npm publish array) | MÉDIO |
| `.mcp.json` | mega-brain-knowledge server | BAIXO |

---

## 6. Estratégia de Migração Segura

### Abordagem: Symlink + Alias (RECOMENDADA)

Em vez de renomear `knowledge/` → `knowledge/external/`, a abordagem mais segura:

1. **Manter** `knowledge/` com subpastas atuais (dna, dossiers, playbooks, sources)
2. **Criar** `knowledge/external/` como **alias/symlink** para as subpastas existentes
3. **Criar** `workspace/` e `knowledge/personal/` como pastas novas
4. **Atualizar** `core/paths.py` com novos paths (KNOWLEDGE_EXTERNAL, KNOWLEDGE_WORKSPACE, KNOWLEDGE_PERSONAL)
5. **Migrar** scripts incrementalmente para usar novos paths

### Alternativa: Mover tudo para knowledge/external/

Mais limpo mas requer atualizar TODOS os 127+ arquivos de uma vez.

---

## 7. Ordem de Atualização (Dependências)

```
1. core/paths.py                    ← PRIMEIRO (single source of truth)
2. core/intelligence/rag/chunker.py ← RAG depende de paths
3. core/intelligence/rag/graph_builder.py
4. core/intelligence/*.py           ← Restante da intelligence
5. .claude/hooks/*.py               ← Hooks
6. agents/cargo/**/DNA-CONFIG.yaml  ← 45+ configs (bulk update)
7. bin/lib/installer.js             ← npm scaffold
8. bin/utils/pro-detector.js        ← Pro detection
9. .gitignore                       ← Layer rules
10. package.json                    ← npm publish
11. CLAUDE.md                       ← Documentation
```

---

*Auditoria gerada automaticamente — Fase 0 do PRD Megabrain 3D*
