
#default board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]




game_going = True

winner = None

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#rules of the game, winners, losers, tie.
def play_game():

    display_board()

    while game_going:

     handle_turn(current_player)

     check_if_game_over()

     flip_player()


# For a specific players turn
def handle_turn(player):

    position = input("Choose a position from 1-9:")
    position = int(position) - 1

    board[position] = "X"
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()


#Finding a winner
def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    cross_winner = check_cross()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif cross_winner:
        winner = cross_winner

    else:
        winner = None
    return

def check_rows():

    global game_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_columns():
    
    global game_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
     game_going = False
    if column_1:
     return board[0]
    elif column_2:
     return board[1]
    elif column_3:
     return board[2]
    return

def check_cross():
    global game_going

    cross_1 = board[0] == board[4] == board[8] != "-"
    cross_2 = board[6] == board[4] == board[2] != "-"

    if cross_1 or cross_2:
        game_going = False
    if cross_1:
        return board[0]
    elif cross_2:
        return board[6]
   
    return


#Linked in with cats game
def check_if_tie():
    global game_going
    if "-" not in board:
        game_going = False

    return

def flip_player():
    global current_player
    # if current turn is x, it will change to O
    if current_player == "X":
        current_player = "O"
        #If current turn is O, will change to O
    elif current_player == "O":
        current_player = "X"
    return

play_game()
