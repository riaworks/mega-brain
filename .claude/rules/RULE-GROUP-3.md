---
paths:
  - ".claude/mission-control/**"
  - "core/templates/**"
---

# RULE-GROUP-3: OPERATIONS

> **Auto-Trigger:** Regras de operações, paralelismo e contexto de negócio
> **Keywords:** "terminal", "paralelo", "[SUA EMPRESA]", "template", "log", "chat", "oráculo", "KPI", "métricas"
> **Prioridade:** ALTA
> **Regras:** 15, 16, 17

---

## 🚫 REGRA #15: PARALELISMO DE TERMINAIS

**PARA MÁXIMA PRODUTIVIDADE, USAR MÚLTIPLOS TERMINAIS.**

### Configuração Recomendada:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SETUP DE 5 TERMINAIS:                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TERMINAL 1: PIPELINE PRINCIPAL                                            │
│  └── Processamento de batches, extração de conhecimento                    │
│                                                                             │
│  TERMINAL 2: EXPLORAÇÃO / PESQUISA                                         │
│  └── Buscas no knowledge base, análises ad-hoc                             │
│                                                                             │
│  TERMINAL 3: GERAÇÃO DE OUTPUTS                                            │
│  └── Playbooks, DNAs, agentes                                              │
│                                                                             │
│  TERMINAL 4: LOGS E MONITORAMENTO                                          │
│  └── Verificar logs, estados, progresso                                    │
│                                                                             │
│  TERMINAL 5: TAREFAS AD-HOC                                                │
│  └── Correções, ajustes, experimentos                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Como Abrir:

```
VS Code:  Ctrl+Shift+` (novo terminal) → digitar "claude"
iTerm2:   Cmd+D (split) → digitar "claude"
Ghosty:   Similar ao iTerm2
```

### Benefícios:

- **2-5x mais velocidade** em tarefas paralelas
- **Menos espera** - enquanto um processa, outro trabalha
- **Contextos separados** - cada terminal mantém seu contexto

```
⚠️ TERMINAIS PARALELOS = MULTIPLICADOR DE PRODUTIVIDADE
⚠️ COMPUTADOR AGUENTA - TERMINAL USA MENOS MEMÓRIA QUE IDE
```

---

## 🚫 REGRA #16: CONTEXTO [SUA EMPRESA] OBRIGATÓRIO

**O MEGA BRAIN É O ORÁCULO DA [SUA EMPRESA]. O OBJETIVO É O [META FINANCEIRA].**

### Antes de Qualquer Recomendação Estratégica:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CHECKLIST [SUA EMPRESA] OBRIGATÓRIO:                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [ ] Contexto [SUA EMPRESA] consultado? (/[sua-empresa]/[SUA EMPRESA]-CONTEXT.md)            │
│  [ ] Métricas atuais consideradas? (KPIs, MRR, CAC, LTV)                   │
│  [ ] Impacto no [META FINANCEIRA] calculado?                                          │
│  [ ] Recursos disponíveis verificados? (time, budget)                      │
│  [ ] Time atual pode executar?                                              │
│  [ ] Alinhado com flywheel?                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Arquivos de Contexto OBRIGATÓRIOS:

```
/[sua-empresa]/
├── [SUA EMPRESA]-CONTEXT.md          ← CONTEXTO MASTER (LER SEMPRE)
├── HIRING-STRUCTURE.md        ← Estrutura de contratação
├── AGENT-TALENT.md            ← Agente de recrutamento
└── DRIVE-FOLDER-IDS.json      ← IDs do Google Drive

/knowledge/[SUA EMPRESA]/
├── _INDEX.md                  ← Índice do knowledge [SUA EMPRESA]
└── DOSSIER-RICHARD-LINDER.md  ← Framework Founder First Hiring
```

### Google Drive IDs Críticos:

```yaml
kpis_master: "[YOUR_SHEET_ID_HERE]"
dre_2025: "[YOUR_SHEET_ID_HERE]"
hiring_folder: "[YOUR_FOLDER_ID_HERE]"
```

### Ao Ativar o Conselho de Agentes:

Os agentes especialistas **DEVEM**:
1. **Receber contexto [SUA EMPRESA]** antes de opinar
2. **Considerar métricas reais** (não genéricas)
3. **Propor ações que movem o ponteiro** do [META FINANCEIRA]
4. **Respeitar constraints** de time e recursos

### O Que É Proibido:

- **NÃO PODE** fazer recomendações estratégicas sem consultar [SUA EMPRESA]-CONTEXT.md
- **NÃO PODE** sugerir ações genéricas que não consideram a realidade da empresa
- **NÃO PODE** ignorar métricas atuais ao propor mudanças
- **NÃO PODE** recomendar contratações sem considerar custos fixos atuais
- **DEVE** sempre responder: "Como isso nos aproxima do [META FINANCEIRA]?"

```
⚠️ RECOMENDAÇÃO SEM CONTEXTO [SUA EMPRESA] = RECOMENDAÇÃO INVÁLIDA
⚠️ O ORÁCULO SEM CONTEXTO É APENAS UM CHATBOT
⚠️ COM CONTEXTO, É O CÉREBRO DO [META FINANCEIRA]
```

---

## 🚫 REGRA #17: TEMPLATES E LOGS DEVEM SER EXPOSTOS NO CHAT

**ANTES DE EXECUTAR QUALQUER FASE/SUB-FASE, O TEMPLATE DEVE SER MOSTRADO NO CHAT.**

### Fluxo Obrigatório:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  FLUXO TEMPLATE-FIRST (OBRIGATÓRIO):                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. CRIAR TEMPLATE                                                          │
│     └── Definir estrutura, métricas, cascadeamentos                        │
│                                                                             │
│  2. MOSTRAR NO CHAT                                                         │
│     └── Exibir template COMPLETO com ASCII art                             │
│                                                                             │
│  3. ANÁLISE DE ALOCAÇÃO                                                     │
│     └── Mapear quais artefatos vão para onde                               │
│     └── Identificar todos os incrementos em outras pastas                  │
│                                                                             │
│  4. AGUARDAR APROVAÇÃO                                                      │
│     └── Usuário valida antes de executar                                   │
│                                                                             │
│  5. EXECUTAR                                                                │
│     └── Só após aprovação explícita                                        │
│                                                                             │
│  6. MOSTRAR LOG DE EXECUÇÃO                                                 │
│     └── Exibir resultado COMPLETO no chat                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Template Mínimo Obrigatório:

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    [FASE X.Y] - [NOME DA SUB-FASE]                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  MISSÃO:     [ID]                                                            ║
║  FASE:       [N] - [NOME]                                                    ║
║  SUB-FASE:   [X.Y] - [NOME]                                                  ║
║  STATUS:     [PENDING/IN_PROGRESS/COMPLETE]                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─ INPUT ─────────────────────────────────────────────────────────────────────┐
│  O que entra nesta sub-fase (arquivos, dados, dependências)                 │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ OUTPUT ────────────────────────────────────────────────────────────────────┐
│  O que será criado/modificado (arquivos, artefatos)                         │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ CASCADEAMENTOS ────────────────────────────────────────────────────────────┐
│  ⚠️ CRÍTICO: Quais outras pastas/arquivos são afetados                      │
│                                                                             │
│  ARTEFATO → EFEITOS DOWNSTREAM                                              │
│  ├── [Artefato 1]                                                           │
│  │   ├── → Atualiza [arquivo X]                                             │
│  │   ├── → Referenciado por [agent Y]                                       │
│  │   └── → Cross-ref em [dossier Z]                                         │
│  └── [Artefato 2]                                                           │
│      └── → Indexado em [_INDEX.md]                                          │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ MÉTRICAS ──────────────────────────────────────────────────────────────────┐
│  Arquivos a criar: X    Arquivos a modificar: Y    Referências: Z           │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ PRÓXIMA SUB-FASE ──────────────────────────────────────────────────────────┐
│  [X.Y+1] - [Nome] - Dependências: [lista]                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Regras Absolutas:

- **NÃO PODE** executar fase sem primeiro criar e MOSTRAR o template no chat
- **NÃO PODE** salvar log apenas em arquivo sem exibir visualmente no chat
- **NÃO PODE** avançar sem mapear TODOS os cascadeamentos
- **NÃO PODE** executar sem aprovação explícita do usuário
- **DEVE** mostrar ASCII header + INPUT + OUTPUT + CASCADEAMENTOS ANTES de executar
- **DEVE** aguardar "ok", "aprovo", "continua" ou similar antes de avançar
- **DEVE** após execução, exibir log completo no chat (não apenas "criado com sucesso")

### Gatilhos de Ativação:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  QUANDO APLICAR ESTA REGRA:                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  ✓ Início de qualquer fase (1, 2, 3, 4, 5)                                  │
│  ✓ Início de qualquer sub-fase (5.1, 5.2, 5.3, etc.)                        │
│  ✓ Criação de novos artefatos que afetam múltiplas pastas                   │
│  ✓ Operações com cascadeamentos complexos                                   │
│  ✓ Quando há dúvida sobre alocação de informação                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
⚠️ TEMPLATE NÃO MOSTRADO = EXECUÇÃO PROIBIDA
⚠️ LOG NÃO EXIBIDO NO CHAT = TRABALHO INCOMPLETO
⚠️ CASCADEAMENTOS NÃO MAPEADOS = RISCO DE INCONSISTÊNCIA
⚠️ SEMPRE TEMPLATE-FIRST. SEMPRE NO CHAT. SEMPRE.
```

---

## 📋 CHECKLIST RÁPIDO - OPERATIONS

```
[ ] Usando múltiplos terminais para produtividade?
[ ] Recomendação estratégica? Consultei [SUA EMPRESA]-CONTEXT.md?
[ ] Métricas [SUA EMPRESA] consideradas (MRR, CAC, LTV)?
[ ] Template mostrado no chat ANTES de executar?
[ ] Cascadeamentos todos mapeados?
[ ] Aprovação obtida antes de avançar?
[ ] Log completo exibido no chat após execução?
```

---

**FIM DO RULE-GROUP-3**
