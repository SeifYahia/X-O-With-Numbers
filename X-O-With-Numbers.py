# Description: Tic-Tac-Toe Game With Numbers
# Version: 1.0
# Date: 26 Feb. 2022

board = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
board_status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
odd = [i for i in range(1, 11, 2)]
even = [j for j in range(0, 10, 2)]


# Display game board to players to start the game
def display_board():
    print ("\n+-----------------+")
    print ("| ", board[0], " | ", board[1], " | ", board[2], " |")
    print ("+-----------------+")
    print ("| ", board[3], " | ", board[4], " | ", board[5], " |")
    print ("+-----------------+")
    print ("| ", board[6], " | ", board[7], " | ", board[8], " |")
    print ("+-----------------+\n")


# Take input as odd or even numbers from players
def take_move(player):
    num = player + " player, please choose a number from "
    if(player == "First"):
        num = num + str(odd) + " : "
    elif(player == "Second"):
        num = num + str(even) + " : "
    valid = False
    # Check if the input is correct or not
    # And if not print an error message
    # Then take the input again untill it's correct
    while(not valid):
        turn = input(num)
        if(turn.isdigit()):
            turn = int(turn)
        else:
            print('INVALID INPUT!!', end=' ')
            continue
        if(player == 'First' and turn not in odd):
            print('Choose a number from the list!!', end=' ')
            continue
        elif(player == 'First' and turn in odd):
            # Remove the selected number from the list
            # So it cannot be selected again
            odd.remove(turn)
            valid = True
        if(player == 'Second' and turn not in even):
            print('Choose a number from the list!!', end=' ')
            continue
        elif(player == 'Second' and turn in even):
            # Remove the selected number from the list
            # So it cannot be selected again
            even.remove(turn)
            valid = True
        else:
            break
    return turn


# Get the place where the player wants to put the number in
def get_place():
    print("The default of all cells is 0.")
    message = "Please, choose a cell from A to I to put the number in: "
    # Check if the input is correct or not
    # And if not print an error message
    # Then take the input again untill it's correct
    while True:
        letter = input(message)
        if (letter not in board):
            print('INVALID INPUT!!', end=' ')
            continue
        else:
            break
    # Attach the selected letter to its index in the list
    if(letter == 'A'):
        letter = 0
    elif(letter == 'B'):
        letter = 1
    elif(letter == 'C'):
        letter = 2
    elif(letter == 'D'):
        letter = 3
    elif(letter == 'E'):
        letter = 4
    elif(letter == 'F'):
        letter = 5
    elif(letter == 'G'):
        letter = 6
    elif(letter == 'H'):
        letter = 7
    elif(letter == 'I'):
        letter = 8

    return letter


# Update the game board according to the inputs of the players
def update_game_board(action, place):
    # Replace the index of the letter selected with the number selected
    board[place] = action
    board_status[place] = action
    # Display board after updates
    display_board()


# Check if there is a winner or no
def is_winner():
    diag1 = board_status[0] + board_status[4] + board_status[8]
    diag2 = board_status[2] + board_status[4] + board_status[6]
    row1 = board_status[0] + board_status[1] + board_status[2]
    row2 = board_status[3] + board_status[4] + board_status[5]
    row3 = board_status[6] + board_status[7] + board_status[8]
    col1 = board_status[0] + board_status[3] + board_status[6]
    col2 = board_status[1] + board_status[4] + board_status[7]
    col3 = board_status[2] + board_status[5] + board_status[8]

    # Check if the sum of any diagonal or vertical or
    # horizontal line is equal to 15
    if(diag1 == 15 or diag2 == 15 or row1 == 15 or row2 == 15 or
            row3 == 15 or col1 == 15 or col2 == 15 or col3 == 15):
        return True
    else:
        return False


# Main function to play the game
def play():
    print('''\nWelcome to the Tic-Tac-Toe game with numbers.
In this game each player chooses a number from odd or even numbers.
The first player chooses the odd numbers from 1 to 9.
The second player chooses the even numbers from 0 to 8.
The first one to complete a line of numbers that sum up to 15 is the winner!
Good Luck!!''')
    display_board()
    n_actions = 0
    while(n_actions != 9):
        move = take_move('First')
        location = get_place()
        update_game_board(move, location)
        if(is_winner()):
            print ('Congratulations!! First player has won.\n')
            break
        n_actions += 1
        if(n_actions == 9):
            break

        move = take_move('Second')
        location = get_place()
        update_game_board(move, location)
        if(is_winner()):
            print ('Congratulations!! Second player has won.\n')
            break
        n_actions += 1

    if(not is_winner()):
        print('The game is draw!\n')

play()
