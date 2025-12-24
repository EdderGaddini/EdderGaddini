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
   - Adicione a label `approved`
   - A jogada será executada automaticamente
   - O tabuleiro será atualizado
   - A Issue será fechada

4. **Para rejeitar:**
   - Apenas feche a Issue com um comentário
   - Remova a label `awaiting-approval`

## Labels do Sistema

- 🟢 `chess-move` - Marca todas as Issues de xadrez
- 🟡 `awaiting-approval` - Aguardando sua revisão
- 🔵 `approved` - Jogada aprovada (executa automaticamente)
- 🔴 `invalid-move` - Jogada inválida (fechada automaticamente)

## Comandos Especiais

Você pode criar Issues manualmente com:

- `chess|reset` - Reinicia o jogo (adicione label `approved`)

## Dicas

- Confira `chess.pgn` para ver o histórico completo
- O arquivo `chess_board.svg` é atualizado automaticamente
- Todas as jogadas são commitadas pelo bot

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
