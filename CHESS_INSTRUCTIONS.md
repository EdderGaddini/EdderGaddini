# 🎮 Jogo de Xadrez no Perfil do GitHub

Este repositório contém um jogo de xadrez interativo que funciona através de GitHub Issues com sistema de aprovação!

## 🎯 Como Jogar

### Para Jogadores:

1. **Vá até o [README.md](./README.md)** e clique em uma das jogadas sugeridas
   - Ou crie uma nova Issue manualmente com título `chess|[jogada]`
   
2. **Aguarde a validação automática**
   - O bot irá verificar se a jogada é válida
   - Se válida: receberá a label `awaiting-approval`
   - Se inválida: a Issue será fechada com explicação

3. **Aguarde aprovação do mantenedor**
   - @EdderGaddini irá revisar e adicionar a label `approved`
   - A jogada será executada automaticamente
   - O tabuleiro será atualizado no README!

### Para o Mantenedor (@EdderGaddini):

1. **Revise as Issues** com label `awaiting-approval`
2. **Adicione a label `approved`** para executar a jogada
3. **Ou feche a Issue** se quiser rejeitar a jogada

## 📋 Exemplos de Jogadas

**Aberturas populares:**
- `chess|e2e4` - Abertura do Rei
- `chess|d2d4` - Abertura da Dama  
- `chess|c2c4` - Abertura Inglesa
- `chess|g1f3` - Abertura Réti

**Respostas comuns:**
- `chess|e7e5` - Defesa do Rei
- `chess|c7c5` - Defesa Siciliana
- `chess|e7e6` - Defesa Francesa
- `chess|c7c6` - Defesa Caro-Kann

## Notação UCI

A notação UCI usa coordenadas do tabuleiro:
- Colunas: a-h (da esquerda para a direita)
- Linhas: 1-8 (de baixo para cima)
- Formato: `[origem][destino]`
- Promoção: adicione a peça (q=dama, r=torre, b=bispo, n=cavalo)
  - Exemplo: `e7e8q` (peão promovido a dama)

## Recursos

- ♟️ Tabuleiro SVG atualizado automaticamente
- 📊 Histórico completo de jogadas em formato PGN
- ✅ Validação de jogadas legais
- 🎯 Detecção de xeque, xeque-mate e empate
- 🤝 Comunidade joga colaborativamente

## Arquivos

- `chess.pgn` - Histórico do jogo em formato PGN
- `chess_board.svg` - Visualização atual do tabuleiro
- `chess_game.py` - Script Python que gerencia o jogo
- `.github/workflows/chess.yml` - GitHub Action que processa as jogadas

## Comandos Especiais

Você também pode criar Issues com:
- `chess|reset` - Reinicia o jogo (apenas mantenedores)

## Tecnologias

- Python 3.10+
- python-chess library
- GitHub Actions
- SVG para visualização

---

Divirta-se jogando! ♟️🎉
