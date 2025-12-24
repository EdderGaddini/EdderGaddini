# ⚙️ Configuração do Workflow

Este diretório contém a configuração do GitHub Actions para o jogo de xadrez interativo.

## Arquivos

### workflows/chess.yml
Workflow principal que gerencia o jogo de xadrez:

#### Triggers (Gatilhos):
- `workflow_dispatch`: Permite execução manual
- `issues.opened`: Quando uma nova Issue é criada
- `issues.labeled`: Quando uma label é adicionada a uma Issue

#### Jobs:

**1. validate-move**
- Executa quando: Issue criada com título `chess|*`
- Função: Valida se a jogada é legal
- Saída: 
  - Se válida: adiciona labels `chess-move` e `awaiting-approval`
  - Se inválida: fecha a Issue com mensagem de erro

**2. execute-move**
- Executa quando: Label `approved` é adicionada
- Função: Executa a jogada aprovada
- Ações:
  - Atualiza `chess.pgn` (histórico)
  - Atualiza `chess_board.svg` (visual)
  - Atualiza `README.md` (estado do jogo)
  - Comenta e fecha a Issue

### ISSUE_TEMPLATE/chess-move.yml
Template para facilitar a criação de Issues de jogadas.

### labels.yml
Definição das labels usadas no projeto:
- `chess-move`: Marca Issues de xadrez
- `awaiting-approval`: Aguardando aprovação
- `approved`: Jogada aprovada (trigger de execução)
- `invalid-move`: Jogada inválida

## Permissões Necessárias

O workflow precisa das seguintes permissões (já configuradas no arquivo):

```yaml
permissions:
  contents: write  # Para commitar mudanças
  issues: write    # Para gerenciar Issues
```

## Variáveis de Ambiente

O workflow usa:
- `GITHUB_TOKEN`: Token automático fornecido pelo GitHub
- Nenhuma variável secreta adicional é necessária

## Fluxo de Execução

```
Issue criada (chess|e2e4)
    ↓
validate-move job
    ↓
Se válida: adiciona labels
    ↓
Mantenedor adiciona label "approved"
    ↓
execute-move job
    ↓
Atualiza arquivos e comenta
```

## Modificações

Se precisar modificar o workflow:

1. Edite `.github/workflows/chess.yml`
2. Teste localmente primeiro
3. Faça commit e push
4. Teste com uma Issue de exemplo

## Debug

Para ver logs detalhados:
1. Vá em **Actions**
2. Selecione a execução
3. Expanda os steps

---

Criado com ❤️ usando GitHub Actions
