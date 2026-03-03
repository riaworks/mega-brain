#!/usr/bin/env python3
"""
JARVIS Post Tool Use Hook
Executado após Claude Code usar uma ferramenta de edição/escrita.

Responsabilidades:
1. Registrar arquivos modificados
2. Detectar padrões
3. Sugerir melhorias quando apropriado
4. REGRA #27.2: Rastrear agente ativo via Skill tool
"""

import json
import sys
import os
import re
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get('CLAUDE_PROJECT_DIR', '.'))


def get_project_dir():
    """Obtém o diretório do projeto."""
    return str(PROJECT_ROOT)


def detect_agent_activation(tool_name: str, tool_input: dict) -> str | None:
    """
    REGRA #27.2: Detecta se a Skill tool ativou um agente.

    Retorna o nome do agente se detectado, None caso contrário.

    Padrões detectados:
    - Skill tool com skill="AIOS:agents:architect"
    - Skill tool com skill="AIOS:agents:dev"
    - Etc.
    """
    if tool_name != "Skill":
        return None

    skill_name = tool_input.get("skill", "")

    # Padrão: AIOS:agents:{agent-name}
    match = re.match(r'^AIOS:agents:([a-zA-Z0-9_-]+)$', skill_name)
    if match:
        return match.group(1)

    # Padrão alternativo: apenas o nome do agente se vier de slash command
    if skill_name and ":" not in skill_name:
        known_agents = [
            "dev", "qa", "architect", "pm", "po", "sm", "analyst",
            "devops", "data-engineer", "aios-master", "doc-master",
            "closer", "bdr", "sds", "lns", "sales-squad",
            "cro", "cfo", "cmo", "coo",
            "alex-hormozi", "cole-gordon", "jeremy-miner", "jeremy-haynes",
            "design-system", "ux-design-expert", "bilhon-docs", "obsidian-ui"
        ]
        if skill_name.lower() in known_agents:
            return skill_name.lower()

    return None


def update_agent_active(agent_name: str | None) -> bool:
    """
    Atualiza o campo agent_active no STATE.json.

    Args:
        agent_name: Nome do agente ou None para limpar

    Returns:
        True se atualizou com sucesso, False caso contrário
    """
    state_path = PROJECT_ROOT / ".claude" / "jarvis" / "STATE.json"

    if not state_path.exists():
        return False

    try:
        with open(state_path, 'r', encoding='utf-8') as f:
            state = json.load(f)

        if "session" not in state:
            state["session"] = {}

        state["session"]["agent_active"] = agent_name
        state["session"]["last_action_at"] = datetime.now().isoformat()

        if agent_name:
            state["session"]["is_active"] = True

        with open(state_path, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

        return True
    except Exception:
        return False


def load_actions_log():
    """Carrega log de ações."""
    log_path = PROJECT_ROOT / 'logs' / 'actions.json'

    if log_path.exists():
        with open(log_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'actions': []}

def save_actions_log(log):
    """Salva log de ações."""
    log_path = PROJECT_ROOT / 'logs' / 'actions.json'
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Manter apenas últimas 100 ações
    log['actions'] = log['actions'][-100:]

    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=2, ensure_ascii=False)

def detect_patterns(actions):
    """Detecta padrões nas ações recentes."""
    if len(actions) < 3:
        return None
    
    # Verificar se mesmo arquivo foi editado múltiplas vezes
    recent = actions[-10:]
    file_counts = {}
    for action in recent:
        file_path = action.get('file_path', '')
        if file_path:
            file_counts[file_path] = file_counts.get(file_path, 0) + 1
    
    # Se algum arquivo foi editado 3+ vezes
    repeated = [f for f, c in file_counts.items() if c >= 3]
    if repeated:
        return {
            'type': 'repeated_edits',
            'files': repeated,
            'suggestion': 'Arquivo editado múltiplas vezes. Considerar refatoração.'
        }
    
    return None

def main():
    """Função principal do hook."""
    try:
        # Ler input do hook (stdin)
        input_data = sys.stdin.read()
        hook_input = json.loads(input_data) if input_data else {}
        
        # Extrair informações da ferramenta
        tool_name = hook_input.get('tool_name', 'unknown')
        tool_input = hook_input.get('tool_input', {})
        
        file_path = tool_input.get('file_path', '')

        # === REGRA #27.2: DETECTAR ATIVAÇÃO DE AGENTE ===
        agent_activated = detect_agent_activation(tool_name, tool_input)
        if agent_activated:
            update_agent_active(agent_activated)

        # Carregar log
        log = load_actions_log()

        # Registrar ação
        action = {
            'timestamp': datetime.now().isoformat(),
            'tool': tool_name,
            'file_path': file_path,
            'session_id': hook_input.get('session_id', 'unknown')
        }

        # Se agente foi ativado, registrar no log
        if agent_activated:
            action['agent_activated'] = agent_activated

        log['actions'].append(action)
        
        # Salvar log
        save_actions_log(log)
        
        # Detectar padrões
        pattern = detect_patterns(log['actions'])
        
        # Preparar feedback
        feedback = None
        if pattern:
            feedback = f"[JARVIS] Padrão detectado: {pattern['suggestion']}"
        
        output = {
            'continue': True,
            'feedback': feedback
        }
        
        print(json.dumps(output))
        
    except Exception as e:
        # Em caso de erro, não bloquear a operação
        error_output = {
            'continue': True,
            'feedback': None
        }
        print(json.dumps(error_output))

if __name__ == '__main__':
    main()
