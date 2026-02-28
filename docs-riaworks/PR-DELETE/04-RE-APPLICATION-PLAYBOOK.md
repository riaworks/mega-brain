# Playbook de Re-aplicação dos Fixes

## Pré-requisitos

- Fork `riaworks/mega-brain` recriado limpo (sem commit c174302 no histórico)
- Backup confirmado em `riaworks/mega-brain-bkp` (privado)
- Pasta `docs-riaworks/PR-DELETE/` disponível localmente

## Passo 1: Atualizar Remotes Locais

```bash
cd /c/__thiago/mega-brain

# Remover remote antigo e adicionar o novo fork
git remote remove origin
git remote add origin https://github.com/riaworks/mega-brain.git
git fetch origin

# Reset main local para o fork limpo
git checkout main
git reset --hard origin/main

# Limpar branches antigas
git branch -D fix/permissions-hardening 2>/dev/null
git branch -D fix/cicd-security-hardening 2>/dev/null

# Verificar: NÃO deve retornar nada
git log --all --oneline -- docs-riaworks/
```

## Passo 2: Re-aplicar PR1 (CI/CD Hardening)

```bash
git checkout -b fix/cicd-security-hardening

# Aplicar patch
git apply docs-riaworks/PR-DELETE/01-PR1-CICD-HARDENING/full-diff.patch

# Se patch falhar, copiar arquivos:
# cp docs-riaworks/PR-DELETE/01-PR1-CICD-HARDENING/files/*.yml .github/workflows/

git add .github/workflows/
git commit -m "fix(security): CI/CD command injection + supply chain hardening [CRITICAL]

Findings: C-01, M-01, L-01, L-02, L-08

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

git push -u origin fix/cicd-security-hardening
gh pr create --repo riaworks/mega-brain --base main --head fix/cicd-security-hardening \
  --title "fix(security): CI/CD command injection + supply chain hardening" \
  --body "Fixes C-01 (command injection), M-01 (TruffleHog pinning), L-01/L-02 (SHA pinning), L-08 (docs)"
```

## Passo 3: Merge PR1, depois Re-aplicar PR2

```bash
# Após PR1 mergeada:
git checkout main && git pull origin main
git checkout -b fix/permissions-hardening

# Aplicar patches
git apply docs-riaworks/PR-DELETE/02-PR2-PERMISSIONS-HARDENING/files/settings.json.diff
git add .claude/settings.json
git commit -m "fix(security): add missing timeouts to hooks

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

cp docs-riaworks/PR-DELETE/02-PR2-PERMISSIONS-HARDENING/files/settings.local.example.json .claude/
git add .claude/settings.local.example.json
git commit -m "docs(security): add hardened settings.local.example.json template

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

git push -u origin fix/permissions-hardening
gh pr create --repo riaworks/mega-brain --base main --head fix/permissions-hardening \
  --title "fix(security): permissions hardening + deny list + hook timeouts" \
  --body "Fixes C-02, C-03, C-04, L-05, L-06, L-13"
```

## Passo 4: PR Cross-Fork para Upstream (depois de merge no fork)

```bash
# Após AMBAS PRs mergeadas no fork:
gh pr create --repo thiagofinch/mega-brain --head riaworks:main --base main \
  --title "fix(security): CI/CD hardening + permissions + deny lists" \
  --body "Security fixes without internal audit documentation"
```

## Passo 5: Verificação Final

```bash
# Confirmar que docs-riaworks/ NÃO está no histórico do novo fork
git log --all --oneline -- docs-riaworks/
# Deve retornar VAZIO

# Confirmar backup existe e é privado
gh repo view riaworks/mega-brain-bkp --json visibility
# Deve retornar: PRIVATE
```
