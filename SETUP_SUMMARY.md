# ♟️ Sistema de Xadrez Comunitário - Resumo

## 🎯 Como Funciona

```
┌─────────────────────────────────────────────────────────────┐
│  1. Jogador clica no link ou cria Issue: chess|e2e4         │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  2. GitHub Action valida automaticamente                     │
│     ✓ Jogada válida? → Adiciona label "awaiting-approval"   │
│     ✗ Jogada inválida? → Fecha Issue                        │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Você (@EdderGaddini) revisa                             │
│     → Adiciona label "approved" para aceitar                │
│     → OU fecha a Issue para rejeitar                        │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  4. GitHub Action executa a jogada                          │
│     → Atualiza chess.pgn (histórico)                        │
│     → Atualiza chess_board.svg (visual)                     │
│     → Atualiza README.md (estado do jogo)                   │
│     → Comenta na Issue e fecha                              │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Estrutura de Arquivos

```
EdderGaddini/
├── .github/
│   ├── workflows/
│   │   └── chess.yml              # Automação principal
│   ├── ISSUE_TEMPLATE/
│   │   └── chess-move.yml         # Template de Issue
│   └── labels.yml                 # Labels do projeto
│
├── chess_game.py                  # Motor do jogo (Python)
├── chess.pgn                      # Histórico de jogadas
├── chess_board.svg                # Tabuleiro visual
├── requirements.txt               # Dependências Python
├── README.md                      # Página principal (com tabuleiro)
├── CHESS_INSTRUCTIONS.md          # Instruções para jogadores
└── MAINTAINER_GUIDE.md            # Seu guia de aprovação
```

## 🎮 Exemplos de Uso

### Jogador sugere jogada:
```
Título da Issue: chess|e2e4
Label automática: awaiting-approval
```

### Você aprova:
```
Ação: Adicionar label "approved"
Resultado: Jogada executada, tabuleiro atualizado!
```

### Você rejeita:
```
Ação: Fechar Issue (opcional: comentar o motivo)
Resultado: Nada acontece com o jogo
```

## 🔧 Configurações Importantes

### Permissões do GitHub Actions
O workflow precisa de:
- ✅ `contents: write` - Para commitar arquivos
- ✅ `issues: write` - Para gerenciar Issues

### Labels Necessárias
Crie estas labels no repositório:
- `chess-move` (verde)
- `awaiting-approval` (amarelo)
- `approved` (azul)
- `invalid-move` (vermelho)

## 🚀 Próximos Passos

1. **Faça commit de todos os arquivos**
   ```bash
   git add .
   git commit -m "♟️ Adiciona jogo de xadrez interativo"
   git push
   ```

2. **Crie as labels manualmente** ou use o arquivo `.github/labels.yml`

3. **Teste o sistema**:
   - Crie uma Issue teste: `chess|e2e4`
   - Veja a validação automática
   - Adicione label `approved`
   - Veja a jogada ser executada!

4. **Compartilhe com a comunidade!**

---

**Feito com ❤️ e Python**
