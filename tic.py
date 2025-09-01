import math

# Constants
HUMAN = 'x'
AI = 'O'
EMPTY = ' '

# Initialize board
board = [[EMPTY for _ in range(4)] for _ in range(4)]

def print_board():
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 15)

def is_winner(player):
    # Rows, columns and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def is_draw():
    return all([cell != EMPTY for row in board for cell in row])

def minimax(depth, is_maximizing):
    if is_winner(AI):
        return 1
    if is_winner(HUMAN):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        i, j = move
        board[i][j] = AI
        print(f"AI placed {AI} at position ({i+1}, {j+1})")

def human_move():
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] == EMPTY:
                board[row][col] = HUMAN
                break
            else:
                print("That cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers from 1 to 3.")

def play_game():
    print("Welcome to Tic-Tac-Toe AI (Minimax Edition) 🎯")
    print("You are 'O' and AI is 'X'")
    print_board()

    while True:
        human_move()
        print_board()
        if is_winner(HUMAN):
            print("You win! 🎉")
            break
        if is_draw():
            print("It's a draw! 🤝")
            break

        ai_move()
        print_board()
        if is_winner(AI):
            print("AI wins! 😈")
            break
        if is_draw():
            print("It's a draw! 🤝")
            break

# Run the game
if __name__ == "__main__":
    play_game()
