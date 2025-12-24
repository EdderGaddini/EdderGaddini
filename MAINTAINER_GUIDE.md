# 🎮 Guia do Mantenedor - Jogo de Xadrez

## Como Funciona o Sistema

### Fluxo Automático:

1. **Usuário cria Issue** com formato `chess|e2e4`
2. **GitHub Action valida** automaticamente a jogada
3. **Se válida**: Adiciona labels `chess-move` e `awaiting-approval`
4. **Se inválida**: Fecha a Issue com mensagem explicativa

### Seu Papel (Aprovação):

1. **Acesse Issues** com label `awaiting-approval`
2. **Revise a jogada** proposta
3. **Para aprovar:**
   - Abra a Issue
   - No lado direito, clique em "Labels"
   - Adicione a label `approved`
   - Pronto! O bot faz o resto automaticamente:
     - Executa a jogada
     - Atualiza o tabuleiro
     - Remove a label `awaiting-approval`
     - Comenta o resultado
     - Fecha a Issue

4. **Para rejeitar:**
   - Apenas feche a Issue com um comentário explicando o motivo
   - Não precisa remover labels manualmente

## Labels do Sistema

- 🟢 `chess-move` - Marca todas as Issues de xadrez
- 🟡 `awaiting-approval` - Aguardando sua revisão
- 🔵 `approved` - Jogada aprovada (executa automaticamente)
- 🔴 `invalid-move` - Jogada inválida (fechada automaticamente)

## Comandos Especiais

Você pode criar Issues manualmente com:

- `chess|reset` - Reinicia o jogo (adicione label `approved`)

## Dicas

- Confira `chess.pgn` para ver o histórico completo de jogadas
  - Formato: PGN (Portable Game Notation)
  - Inclui: data, evento, todas as jogadas e resultado
- O arquivo `chess_board.svg` é atualizado automaticamente
- Todas as jogadas são commitadas pelo bot
- O jogo é colaborativo: "Community" joga contra "Community"

## 🔄 Como Resetar o Jogo

### Opção 1: Via Issue (Recomendado)
1. Crie uma Issue com título: `chess|reset`
2. Adicione a label `approved`
3. Pronto! O bot reseta tudo automaticamente

### Opção 2: Manual (Terminal)
```bash
python chess_game.py reset
git add chess.pgn chess_board.svg README.md
git commit -m "♟️ Reinicia jogo de xadrez"
git push
```

## Troubleshooting

Se algo der errado:

```bash
# Teste localmente
python chess_game.py status
python chess_game.py move e2e4 --dry-run

# Reinicie o jogo
python chess_game.py reset
```

---

**Divirta-se sendo o mestre do jogo! ♟️👑**
