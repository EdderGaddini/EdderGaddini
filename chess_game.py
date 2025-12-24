#!/usr/bin/env python3
"""
Script para gerenciar o jogo de xadrez no perfil do GitHub
"""
import chess
import chess.pgn
import chess.svg
import io
import os
from datetime import datetime

def load_game():
    """Carrega o jogo atual do arquivo PGN"""
    try:
        with open('chess.pgn', 'r') as f:
            game = chess.pgn.read_game(f)
            if game is None:
                return chess.Board()
            board = game.board()
            for move in game.mainline_moves():
                board.push(move)
            return board
    except FileNotFoundError:
        return chess.Board()

def save_game(board, move_san=None):
    """Salva o estado atual do jogo no arquivo PGN"""
    game = chess.pgn.Game()
    game.headers["Event"] = "GitHub Profile Chess"
    game.headers["Site"] = "https://github.com/EdderGaddini"
    game.headers["Date"] = datetime.now().strftime("%Y.%m.%d")
    game.headers["Round"] = "1"
    game.headers["White"] = "Community"
    game.headers["Black"] = "Community"
    
    node = game
    temp_board = chess.Board()
    
    for move in board.move_stack:
        node = node.add_variation(move)
    
    if board.is_checkmate():
        game.headers["Result"] = "1-0" if board.turn == chess.BLACK else "0-1"
    elif board.is_stalemate() or board.is_insufficient_material():
        game.headers["Result"] = "1/2-1/2"
    else:
        game.headers["Result"] = "*"
    
    with open('chess.pgn', 'w') as f:
        print(game, file=f)

def generate_board_svg(board):
    """Gera o SVG do tabuleiro"""
    svg = chess.svg.board(
        board=board,
        size=400,
        coordinates=True,
        colors={
            "square light": "#F0D9B5",
            "square dark": "#B58863",
        }
    )
    
    with open('chess_board.svg', 'w') as f:
        f.write(svg)

def make_move(move_str, dry_run=False):
    """Executa uma jogada"""
    board = load_game()
    
    try:
        # Tenta interpretar como UCI (e2e4)
        move = chess.Move.from_uci(move_str)
        if move in board.legal_moves:
            if dry_run:
                return True, f"Jogada {board.san(move)} é válida!"
            
            san = board.san(move)
            board.push(move)
            save_game(board, san)
            generate_board_svg(board)
            return True, f"Jogada {san} executada com sucesso!"
        else:
            return False, f"Jogada ilegal: {move_str}"
    except ValueError:
        try:
            # Tenta interpretar como SAN (Nf3)
            move = board.parse_san(move_str)
            if dry_run:
                return True, f"Jogada {board.san(move)} é válida!"
            
            san = board.san(move)
            board.push(move)
            save_game(board, san)
            generate_board_svg(board)
            return True, f"Jogada {san} executada com sucesso!"
        except ValueError:
            return False, f"Formato de jogada inválido: {move_str}"

def reset_game():
    """Reinicia o jogo"""
    board = chess.Board()
    save_game(board)
    generate_board_svg(board)
    return "Jogo reiniciado!"

def get_game_status():
    """Retorna o status atual do jogo"""
    board = load_game()
    
    status = f"Turno: {'Brancas' if board.turn == chess.WHITE else 'Pretas'}\n"
    status += f"Jogadas: {board.fullmove_number}\n"
    
    if board.is_checkmate():
        winner = "Pretas" if board.turn == chess.WHITE else "Brancas"
        status += f"XEQUE-MATE! {winner} vencem!\n"
    elif board.is_check():
        status += "XEQUE!\n"
    elif board.is_stalemate():
        status += "EMPATE por afogamento!\n"
    elif board.is_insufficient_material():
        status += "EMPATE por material insuficiente!\n"
    
    return status

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python chess_game.py <comando> [argumentos]")
        print("Comandos: move <jogada> [--dry-run], reset, status")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "move" and len(sys.argv) >= 3:
        dry_run = "--dry-run" in sys.argv
        move_arg = sys.argv[2]
        success, message = make_move(move_arg, dry_run=dry_run)
        print(message)
        sys.exit(0 if success else 1)
    elif command == "reset":
        print(reset_game())
    elif command == "status":
        print(get_game_status())
    elif command == "init":
        # Inicializa o jogo
        board = chess.Board()
        save_game(board)
        generate_board_svg(board)
        print("Jogo inicializado!")
    else:
        print("Comando inválido")
        sys.exit(1)
