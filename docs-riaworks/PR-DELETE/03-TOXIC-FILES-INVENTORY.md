# Inventário de Arquivos Expostos

**Commit tóxico:** `c174302` ("before-corrections-security")

## Arquivos Commitados (9 — expostos via PR cross-fork)

| Arquivo | Linhas | Conteúdo |
|---------|--------|----------|
| `docs-riaworks/security-reports/security-audit-report.md` | 285 | Relatório completo de auditoria |
| `docs-riaworks/security-reports/cyber-intelligence-report.md` | 339 | Análise de inteligência cibernética |
| `docs-riaworks/security-reports/recommendations.md` | 229 | 13 recomendações priorizadas |
| `docs-riaworks/security-reports/SECURITY-REMEDIATION-PLAN.md` | 461 | Plano de remediação com 7 PRs |
| `docs-riaworks/HANDOFFS/SECURITY1-HANDOFF.md` | 160 | Handoff sessão 1 |
| `docs-riaworks/HANDOFFS/SECURITY2-HANDOFF.md` | 58 | Handoff sessão 2 |
| `docs-riaworks/scan-scripts/README.md` | 7 | Readme dos scripts |
| `docs-riaworks/scan-scripts/generate_inventory.py` | 36 | Script de inventário |
| `docs-riaworks/file-inventory.json` | 7107 | Inventário completo do repositório |

## Arquivos Nunca Commitados (2 — seguros, apenas locais)

| Arquivo | Status |
|---------|--------|
| `docs-riaworks/HANDOFFS/SECURITY3-HANDOFF.md` | Untracked (nunca no git) |
| `docs-riaworks/HANDOFFS/SECURITY4-HANDOFF.md` | Untracked (nunca no git) |

## Risco

Estes arquivos contêm o mapa completo de vulnerabilidades do repositório, incluindo:
- 21 findings válidos com localização exata (6 findings de permissões foram invalidados — baseados em arquivo customizado do usuario)
- Vetores de ataque detalhados
- Plano de remediação com cronograma
- Inventário de todos os arquivos do repositório
