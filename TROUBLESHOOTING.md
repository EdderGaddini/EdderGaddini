# 🔧 Troubleshooting - Jogo de Xadrez

## Problemas Comuns e Soluções

### ❌ GitHub Action não está sendo executada

**Problema:** Ao criar uma Issue com `chess|e2e4`, nada acontece.

**Soluções:**
1. Verifique se o workflow está habilitado:
   - Vá em **Settings** → **Actions** → **General**
   - Certifique-se que Actions está habilitado
   
2. Verifique as permissões:
   - **Settings** → **Actions** → **General** → **Workflow permissions**
   - Selecione "Read and write permissions"
   - Marque "Allow GitHub Actions to create and approve pull requests"

### ❌ Jogada válida mas não executa

**Problema:** A jogada foi validada mas não executa quando você adiciona a label `approved`.

**Solução:**
1. Certifique-se de adicionar **exatamente** a label `approved` (minúsculo)
2. Verifique se a Issue tem a label `awaiting-approval` antes
3. Veja os logs do workflow em **Actions** → selecione a execução

### ❌ Tabuleiro não aparece no README

**Problema:** O README mostra um ícone quebrado onde deveria ter o tabuleiro.

**Solução:**
1. Execute manualmente para gerar o tabuleiro:
   ```bash
   python chess_game.py init
   git add chess_board.svg
   git commit -m "Adiciona tabuleiro inicial"
   git push
   ```

2. Aguarde alguns minutos para o cache do GitHub atualizar

### ❌ Jogada inválida aceita ou jogada válida rejeitada

**Problema:** O bot está validando incorretamente as jogadas.

**Solução:**
1. Teste localmente:
   ```bash
   python chess_game.py move e2e4 --dry-run
   ```

2. Verifique o arquivo `chess.pgn` para ver o estado atual:
   ```bash
   cat chess.pgn
   ```

3. Reinicie o jogo se necessário:
   ```bash
   python chess_game.py reset
   git add chess.pgn chess_board.svg
   git commit -m "Reinicia jogo de xadrez"
   git push
   ```

### ❌ Labels não estão sendo adicionadas

**Problema:** O bot não adiciona as labels automaticamente.

**Solução:**
1. Crie as labels manualmente:
   - Vá em **Issues** → **Labels** → **New label**
   - Crie estas labels:
     - `chess-move` (cor: #0E8A16)
     - `awaiting-approval` (cor: #FBCA04)
     - `approved` (cor: #0075CA)
     - `invalid-move` (cor: #D93F0B)

### ❌ Erro "python-chess not found"

**Problema:** O workflow falha dizendo que não encontrou o módulo python-chess.

**Solução:**
O workflow já inclui `pip install python-chess`. Se ainda assim falhar:
1. Verifique o log da Action
2. Pode ser um problema temporário do PyPI
3. Tente executar o workflow novamente

### ❌ Commits não estão sendo feitos

**Problema:** A jogada executa mas não atualiza o repositório.

**Solução:**
1. Verifique as permissões do workflow (veja primeira solução)
2. Certifique-se que o `GITHUB_TOKEN` tem permissões de write

## Testando Localmente

Para testar tudo localmente antes de fazer push:

```bash
# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instalar dependências
pip install python-chess

# Inicializar jogo
python chess_game.py init

# Testar uma jogada (sem executar)
python chess_game.py move e2e4 --dry-run

# Executar uma jogada
python chess_game.py move e2e4

# Ver status do jogo
python chess_game.py status

# Reiniciar o jogo
python chess_game.py reset
```

## Verificar Logs do Workflow

1. Vá em **Actions** no topo do repositório
2. Clique no workflow mais recente
3. Clique em **chess-move** ou **execute-move**
4. Expanda os steps para ver detalhes

## Ainda com problemas?

1. Verifique se todos os arquivos foram commitados:
   ```bash
   git status
   ```

2. Revise o arquivo `.github/workflows/chess.yml`

3. Teste localmente primeiro

4. Crie uma Issue no repositório descrevendo o problema

---

**Lembre-se:** O GitHub Actions pode levar alguns segundos para ser acionado após criar a Issue!
