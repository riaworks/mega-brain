# PR1 — CI/CD Security Hardening

**Commit original:** `20c89f7`
**Branch:** `fix/cicd-security-hardening`
**Status no fork:** MERGED

## Findings Corrigidos (5/27)

| ID | Severidade | Finding | Correção |
|----|-----------|---------|----------|
| **C-01** | CRITICAL | Command injection via `${{ github.event.pull_request.* }}` em blocos `run:` | Migrado para blocos `env:` |
| **M-01** | MEDIUM | `curl \| sh` para TruffleHog (risco supply chain) | Pinned v3.88.22 com SHA |
| **L-01** | LOW | GitHub Actions não pinadas por SHA | Todas pinadas com commit SHA |
| **L-02** | LOW | npm global install sem versão | Adicionado `@latest` explícito |
| **L-08** | LOW | Workflows duplicados sem documentação | Headers de propósito adicionados |

## Arquivos Modificados (6)

| Arquivo | Mudança Principal |
|---------|-------------------|
| `.github/workflows/claude-code-pr.yml` | env: block migration (C-01) |
| `.github/workflows/claude-code-review.yml` | SHA pinning |
| `.github/workflows/claude.yml` | SHA pinning |
| `.github/workflows/publish-pro.yml` | SHA pinning |
| `.github/workflows/publish.yml` | SHA pinning + TruffleHog pin (M-01) |
| `.github/workflows/verification.yml` | SHA pinning |

## Como Re-aplicar

```bash
# Opção A: Patch
git apply 01-PR1-CICD-HARDENING/full-diff.patch

# Opção B: Copiar arquivos finais
cp 01-PR1-CICD-HARDENING/files/*.yml .github/workflows/
```
