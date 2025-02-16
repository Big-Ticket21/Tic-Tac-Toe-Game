import random as rdm
from re import fullmatch

board =  [i for i in range(1, 10)]
user = None
computer = None
turn = None

def print_board():
    row1 = "+---+---+---+"
    row2 = "| {} | {} | {} |"
    for i in range(3):
        print(row1)
        print(row2.format(board[i*3], board[i*3+1], board[i*3+2]))
    print(row1)

def choose_player(prompt):
    global user
    global computer
    while True:
        user = input(prompt)
        if user.lower() not in "x,o":
            print("invalid input, please choose x or o")
        else:
            computer = "o" if user == "x" else "x"
            print("you have selected: " + str(user))
            return

def decide_first_move(user_choice):
    while True:
        global computer
        global user
        global turn
        user_input = input(user_choice)
        choices = ["heads","tails"]
        coin_flip = rdm.choice(choices)
        if user_input.lower() not in choices:
            print("invalid input, please choose heads or tails")
        else:
            if user_input != coin_flip:
                print("the coin landed on " + str(coin_flip) + " you will have the second turn")
                turn = computer
                break
            else:
                print("congrats! the coin laded on " + str(coin_flip) + "," " you will have the first turn")
                print_board()
                turn = user
                break

def player_move(user_move):
    global board
    global user
    while True:
        try:
            move = int(input(user_move))
            if move < 1 or move > 9 or board[move - 1] in ["x", "o"]:
                print("Enter a valid move between 1 and 9 that has not been taken.")
            else:
                board[move - 1] = user
                break
        except ValueError:
            print("Please enter a valid integer between 1 and 9.")

def computer_move():
    global board
    global computer
    available_moves = [i for i in range(1, 10) if isinstance(board[i-1], int)]
    diagonal = [(2, 4, 6), (0, 4, 8)]
    if board[4] == 5:
        board[4] = computer
    else:
        for i in range(0, 9, 3):
            if board[i] == user and board[i] == board[i + 1]:
                board[i+2] = computer
                return
            if board[i] == user and board[i] == board[i + 2]:
                board[i+1] = computer
                return
            if board[i+1] and board[i+1] == user and board[i+1] == board[i+2]:
                board[i] = computer
                return
        for i in range(3):
            if board[i] == user and board[i] == board[i+3]:
                board[i+6] = computer
                return
            if board[i] == user and board[i] == board[i+6]:
                board[i+3] = computer
                return
            if board[i+3] == user and board[i+6] == board[i + 3]:
                board[i] = computer
                return
        for diag in diagonal:
            if board[diag[0]] == user and board[diag[0]] == board[diag[1]]:
                board[diag[2]] = computer
                return
            if board[diag[1]] == user and board[diag[1]] == board[diag[2]]:
                board[diag[0]] = computer
                return
        if available_moves:
            move = rdm.choice(available_moves)
            board[move-1] = computer
            return

def check_winner():
    global board
    global user
    global computer
    global turn
    diagonal = [(2, 4, 6), (0, 4, 8)]
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            print(f"{board[i]} wins on row {i // 3 + 1}!")
            turn = "winner"
            return
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6]:
            print(f"{board[i]} wins on column {i + 1}!")
            turn = "winner"
            return
    for diag in diagonal:
        if board[diag[0]] == board[diag[1]] == board[diag[2]] and board[diag[0]]:
            print(f"{board[diag[0]]} wins on the diagonal!")
            turn = "winner"
            return

def start_up_game():
    global turn
    global board
    global user
    global computer
    board = [i for i in range(1, 10)]
    user = None
    computer = None
    turn = None
    choose_player("choose either x or o: ")
    decide_first_move("choose heads or tails, a coin will flip for the first move: ")

def play_game():
        global turn
        global board
        global user
        global computer
        choose_player("choose either x or o: ")
        decide_first_move("choose heads or tails, a coin will flip for the first move: ")
        while True:
            if all(isinstance(item, str) for item in board):
                print("The board is full, restarting game...")
                turn = "full"
                start_up_game()
                continue
            if turn == user:
                player_move("Choose a number on the board to make your move: ")
                check_winner()
                if turn == "winner":
                    play_again = input("Do you want to play again? Enter yes or no: ")
                    if play_again.lower() == "yes":
                        start_up_game()  # Reset the game
                        continue
                    else:
                        break
                else:
                    turn = computer
            elif turn == computer:
                computer_move()
                check_winner()
                print_board()
                if turn == "winner":
                    play_again = input("Do you want to play again? Enter yes or no: ")
                    if play_again.lower() == "yes":
                        start_up_game()  # Reset the game
                        continue
                    else:
                        break
                else:
                    turn = user

play_game()


