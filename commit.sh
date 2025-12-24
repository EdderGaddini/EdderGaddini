#!/bin/bash

# 🚀 Script para fazer o primeiro commit do jogo de xadrez

echo "♟️  Preparando para fazer commit do jogo de xadrez..."
echo ""

# Adiciona todos os arquivos
git add .

# Mostra o status
echo "📋 Arquivos que serão commitados:"
git status --short
echo ""

# Faz o commit
git commit -m "♟️ Adiciona jogo de xadrez interativo

- Sistema de jogadas via GitHub Issues
- Validação automática de jogadas
- Aprovação manual pelo mantenedor
- Tabuleiro SVG atualizado automaticamente
- Histórico completo em formato PGN
- Templates de Issue e documentação completa"

echo ""
echo "✅ Commit realizado com sucesso!"
echo ""
echo "📤 Para enviar ao GitHub, execute:"
echo "   git push"
echo ""
echo "📖 Próximos passos:"
echo "1. Execute 'git push' para enviar ao GitHub"
echo "2. Vá em Settings → Actions → General"
echo "3. Habilite 'Read and write permissions'"
echo "4. Crie as labels (ou use o arquivo .github/labels.yml)"
echo "5. Teste criando uma Issue: chess|e2e4"
echo "6. Adicione a label 'approved' para executar a jogada"
echo ""
echo "🎮 Divirta-se jogando xadrez no seu perfil!"
