# Experiment No. 6
# Tic-Tac-Toe using Minimax Algorithm

board = [' ' for _ in range(9)]


def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(player):
    positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in positions
    )


def minimax(is_maximizing):
    if winner('O'):
        return 1

    if winner('X'):
        return -1

    if ' ' not in board:
        return 0

    if is_maximizing:
        best = -100

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)

        return best

    else:
        best = 100

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)

        return best


def best_move():
    best_score = -100
    move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move


print("TIC-TAC-TOE USING MINIMAX")

while True:
    display()

    position = int(input("Enter your position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != ' ':
        print("Invalid move!")
        continue

    board[position] = 'X'

    if winner('X'):
        display()
        print("You win!")
        break

    if ' ' not in board:
        display()
        print("Draw!")
        break

    computer_move = best_move()
    board[computer_move] = 'O'

    if winner('O'):
        display()
        print("Computer wins!")
        break

    if ' ' not in board:
        display()
        print("Draw!")
        break