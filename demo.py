#Tic Tac Toe Game

import math

board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        row = "|".join(board[i*3:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("---+---+---")
    print()

# Check for a winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if board is full
def is_board_full():
    return all(cell != ' ' for cell in board)

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Player move
def player_move():
    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if board[pos] == ' ':
                board[pos] = 'X'
                break
            else:
                print("Cell already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number 1-9.")

# Main game loop
def main():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner('X'):
            print("Congratulations! You won!")
            break
        if is_board_full():
            print("It's a tie!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if check_winner('O'):
            print("AI wins! Better luck next time.")
            break
        if is_board_full():
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
