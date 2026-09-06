import random


#printing the board
board = [" ", " ", " ", 
         " ", " ", " ", 
         " ", " ", " "]


def display_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

#choosing who goes first and assigning symbols
#first player = X and second player = O

starting_player = random.choice(["computer", "player"])
if starting_player == "player":
    user_symbol = "X"
    print(f"Your symbol is {user_symbol}")
    computer_symbol = "O"
    print(f"Computers symbol is {computer_symbol}")
else:
    user_symbol = "O"
    print(f"Your symbol is {user_symbol}")
    computer_symbol = "X"
    print(f"Computers symbol is {computer_symbol}")

#checking all winning combinations and winner
def check_winner(board):
        winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

        for combination in winning_combinations:
             a, b, c = combination
             if board[a] == board[b] == board[c] != " ":
                  winner = board[a]
                  return winner

        if " " not in board:
             return "Its a draw"

        return None


#check available moves
def available_move(board):
     available_spaces = []
     for i in range(9):
          if board[i] == " ":
               available_spaces.append(i)
     return available_spaces

#minimax function
def minimax(board, maximizing, depth):

     #checking terminal state
        if check_winner(board) == computer_symbol:
             return 10
        if check_winner(board) == user_symbol:
             return -10 
        if check_winner(board) == "Its a draw":
             return 0

    #for computer turn
    #computer = max and user = min
        if maximizing:
             value = float("-inf")
             for move in available_move(board):
                  board[move] = computer_symbol
                  score = minimax(board, False, depth + 1)
                  board[move] = " "
                  value = max(value, score - depth)

             return value
        else:
             value = float("inf")
             for move in available_move(board):
                  board[move] = user_symbol
                  score = minimax(board, True, depth + 1)
                  board[move] = " "
                  value = min(value, score + depth)

             return value

#return the best move for the computer 
def get_best_move(board):
    best_score = float("-inf")
    best_move = None

    for move in available_move(board):
        board[move] = computer_symbol

        score = minimax(board, False, 1)

        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

                  
#asking the user for their input
display_board()

def user_turn():

    while True:
         try:
            user_input = int(input("Enter your choice(1-9): "))
            while user_input >= 10 or 0 >= user_input:
                 print("Invalid input")
                 user_input = int(input("Enter your choice(1-9): "))

            while board[user_input - 1] != " ":
                print("Invlid Error")
                user_input = int(input("Enter a number "))
                while user_input >= 10 or 0 >= user_input:
                     print("Enter a number between 1 and 9")
                     user_input = int(input("Enter your choice(1-9): "))
            board[user_input - 1] = user_symbol
            display_board()
            break
         except ValueError:
              print("Enter a number")

        #   checking winner
    if check_winner(board) == user_symbol:
        print("You won")
        return True



    return False
              

#computers turn
def computer_turn():
    #computers turn
    computer_move = get_best_move(board)
    if computer_move != None:
        board[computer_move] = computer_symbol
        print("Computer chose:", computer_move + 1)
        display_board()
    
    #check winnr
    if check_winner(board) == computer_symbol:
         print("You lose")
         return True

    return False
          
           
#running the functions
while True:
    if starting_player == "player":
        if user_turn():
            break
        if computer_turn():
            break
    else:
        if computer_turn():
            break
        if user_turn():
            break

    if check_winner(board) == "Its a draw":
         print("its a draw")
         break
        
