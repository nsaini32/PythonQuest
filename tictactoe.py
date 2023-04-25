# This is a simple tic tac toe game in Python

# Define the board as a list of empty spaces
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Function to display the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == player and board[i+1] == player and board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    return False

# Function to play the game
def play_game():
    # Display the initial board
    display_board()

    # Loop until the game is over
    while True:
        # Get player 1's move
        move = int(input("Player 1 (X), enter your move (1-9): "))
        if board[move-1] == " ":
            board[move-1] = "X"
            display_board()
            if check_win("X"):
                print("Player 1 wins!")
                break
        else:
            print("That space is already taken. Please try again.")
            continue

        # Get player 2's move
        move = int(input("Player 2 (O), enter your move (1-9): "))
        if board[move-1] == " ":
            board[move-1] = "O"
            display_board()
            if check_win("O"):
                print("Player 2 wins!")
                break
        else:
            print("That space is already taken. Please try again.")
            continue

# Call the play_game function to start the game
play_game()
