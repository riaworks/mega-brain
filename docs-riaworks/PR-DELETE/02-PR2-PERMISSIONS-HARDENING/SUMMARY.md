# PR2 — Permissions & Deny List Hardening

**Commits originais:** `f54f0f9`, `571b72b`
**Branch:** `fix/permissions-hardening`
**Status no fork:** OPEN (não mergeada)

## Findings Corrigidos (6/27)

| ID | Severidade | Finding | Correção |
|----|-----------|---------|----------|
| **C-02** | CRITICAL | "Bash" irrestrito na allow list | 40+ patterns específicos |
| **C-03** | CRITICAL | Aninhamento duplo de permissions | Estrutura corrigida |
| **C-04** | CRITICAL | Deny list incompleta | 24 regras (curl, wget, .env, .ssh, git push, npm publish) |
| **L-05** | LOW | Deny list desalinhada com ANTHROPIC-STANDARDS.md | Alinhamento completo |
| **L-06** | LOW | 2 hooks sem timeout | `timeout: 30000` adicionado |
| **L-13** | LOW | Write/Edit amplos | Documentados como necessários |

## Arquivos Modificados (2)

| Arquivo | Mudança |
|---------|---------|
| `.claude/settings.json` | +timeout em gsd-check-update.js e gsd-context-monitor.js |
| `.claude/settings.local.example.json` | NOVO — template hardened (139 linhas) |

## Como Re-aplicar

```bash
# Commit 1: timeouts
git apply 02-PR2-PERMISSIONS-HARDENING/files/settings.json.diff
git add .claude/settings.json
git commit -m "fix(security): add missing timeouts to hooks"

# Commit 2: example file
cp 02-PR2-PERMISSIONS-HARDENING/files/settings.local.example.json .claude/
git add .claude/settings.local.example.json
git commit -m "docs(security): add hardened settings.local.example.json template"
```
