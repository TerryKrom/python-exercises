import chess

def print_board(board):
    print(board)

def main():
    board = chess.Board()

    while not board.is_game_over():
        print_board(board)
        move = input("Digite o seu movimento (ex: 'e2e4'): ")
        
        try:
            board.push_san(move)
        except ValueError:
            print("Movimento inválido. Tente novamente.")
        
    print("Fim de jogo. Resultado: " + board.result())

if __name__ == "__main__":
    main()
