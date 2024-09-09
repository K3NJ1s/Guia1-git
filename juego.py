def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("Movimiento inválido. La celda ya está ocupada.")
        return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Bienvenido al Tres en Raya!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Turno del jugador {player}")

        try:
            row = int(input("Ingrese la fila (0, 1, 2): "))
            col = int(input("Ingrese la columna (0, 1, 2): "))
        except ValueError:
            print("Entrada inválida. Ingrese números enteros.")
            continue

        if row not in range(3) or col not in range(3):
            print("Entrada inválida. Ingrese números entre 0 y 2.")
            continue

        if make_move(board, row, col, player):
            print_board(board)

            if check_winner(board, player):
                print(f"¡Jugador {player} gana!")
                break

            if check_draw(board):
                print("¡Es un empate!")
                break

            turn += 1

if __name__ == "__main__":
    main()
