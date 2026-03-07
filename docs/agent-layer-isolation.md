# Agent Layer Isolation

> Mecanismo de isolamento de agentes entre camadas L1/L2/L3.

## Princípio

| Camada | Visibilidade | Exemplo |
|--------|-------------|---------|
| L1 (Public) | Qualquer pessoa | Agent templates, core engine |
| L2 (Premium) | Assinantes | Cargo agents, expert knowledge |
| L3 (Founder) | Apenas fundador | Business data, personal data |

## Mecanismo

### Agentes L1 → L2
- Agentes em L2 ficam em subpasta com regras de .gitignore
- Conhecimento absorvido NÃO é legível por quem só tem acesso L1
- package.json `files` array controla o que é publicado no npm

### Agentes L2 → L3
- Agentes com dados de L3 ficam em knowledge/personal/ (gitignored)
- Workspace agents com dados sensíveis: workspace/_finance/ (gitignored)
- Clone-data de colaboradores: workspace/_team/**/clone-data/ (gitignored)

### Implementação
- `.gitignore` com regras por camada (Tarefa 7.1)
- RAG bucket isolation com indices separados (Tarefa 7.2)
- bucket_router.py com access control por modo de consulta

## Regras

1. Agente L3 NUNCA publicado no npm package
2. Dados financeiros NUNCA em repo público
3. Clone-data de colaboradores NUNCA em L1
4. Personal bucket NUNCA lido sem flag explícito

---
*Documentação conforme PRD Megabrain 3D, Tarefa 7.3*
