# Experiment No. 1
# Tic-Tac-Toe Game

board = [' ' for _ in range(9)]


def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def check_draw():
    return ' ' not in board


def make_move(player):
    while True:
        try:
            position = int(input(f"Player {player}, enter position (1-9): "))

            if position < 1 or position > 9:
                print("Invalid position!")
            elif board[position - 1] != ' ':
                print("Position already occupied!")
            else:
                board[position - 1] = player
                break

        except ValueError:
            print("Please enter a valid number.")


print("TIC-TAC-TOE GAME")
print("Positions are numbered from 1 to 9.")

current_player = 'X'

while True:
    display_board()
    make_move(current_player)

    if check_winner(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break

    if check_draw():
        display_board()
        print("Game Draw!")
        break

    current_player = 'O' if current_player == 'X' else 'X'