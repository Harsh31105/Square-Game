import random

#Defining Box variable as constant for that symbol. 
box = "▢"

#Welcome Message to the User
print("Welcome to The Square Game!\n")

#Input Method:
manner = input("Press 1 to randomly generate the board.\nPress 9 to input the text file")
if manner == "1":
    #Input parameters for the game.
    max_rows = int(input("Enter Maximum No. of Rows:"))
    max_tiles = int(input("Enter Maximum No. of Tiles in each Row:"))

    #Setting up the Board of the Game.
    board = []
    for i in range(0,max_rows):
        board.append(random.randint(1,max_tiles))
    
elif manner == "9":
    file = open("setup.txt", "r")

    board = file.read().replace(' ', '\n').splitlines()

    #Converting the "text" data in the file to integer datatype. 
    for i in range(0, len(board)):
        board[i] = int(board[i])

########################################################################

# print_board (board) -> Image
# This function prints out the current state of the board.
def print_board():
    for i in range(len(board)):
        print("Row-",i, end="  ")
        for i in range(board[i]):
            print(box, end=" ")
        print("")
    print("\n")

########################################################################

print_board() #Prints out the initial state of the board. 

#Asks the user who should make the first move. 
print("\nPress 1, to make the first move.")
print("Press 9, if you'd like the computer to make the first move.")

#This variable stores the value of the user's choice. 
choice = input("What'll it be?")

# Using the previous value, here, we attribute the user's choice to
# a specific 'state' of the program - either "human" or "computer", based
# on the user's input. 
if choice == "1" :
    move = "Human"
elif choice == "9" :
    move = "Computer"
else:
    print("Invalid Input. Start game again..")
    exit()

#######################################################################

# play: ? -> ?
# This function updates the board using the computer's most optimised
# strategy for winning. If it can win, it will.
def play():
    ALL = 0
    for i in range(0,len(board)):
        ALL = ALL ^ board[i]

    row = 0
    tiles = 0

    if ALL == 0 :
        row = random.randint(0,len(board)-1)
        tiles = 0
        if board[row] == 1:
            tiles = 1
        else:
            tiles = random.randint(1,board[row])
        print("Making Random Move... I wonder why..")
    else:
        for j in range(0,len(board)):
            if board[j] > (ALL ^ board[j]):
                row = j
                tiles = board[j] - (ALL ^ board[j])
                break

    board[row] = board[row]-tiles

    #This checks if the no. of tiles in a row is zero. If yes, it removes that
    # row from the board.
    if board[row] == 0:
        board.remove(0)

#######################################################################



# Real-Time functioning of the game. 
while board != []: # The game runs until the board no longer has any tiles on it.

    #Human's Move
    if move == "Human":
        print("\nIt is the Human's Move...")
        row = int(input("Which row do you want to remove tiles from?"))
        if row >= len(board):
            print("No such row exists. Start game again..")
            exit()
        tiles = int(input("How many tiles do you wish to eat?"))
        if tiles > board[row]:
            print("There are not enough tiles. Start the game again...")
            exit()
        elif tiles == 0:
            print("You cannot remove 0 tiles! Start the game again...")
            exit()
        #Updates the board according to the inputs. 
        board[row] = board[row]-tiles

        #This checks if the no. of tiles in a row is zero. If yes, it removes that
        # row from the board.
        if board[row] == 0:
            board.remove(0)

    #Computer's Move
    elif move == "Computer":
        print("\nNow, I shall play my turn...")
        play()

    #Prepares the game for the next move. 
    if board == []:
        break
    else:
        print_board()
        if move == "Human":
            move = "Computer"
        elif move == "Computer":
            move = "Human"

#Determines who won the game. 
if move == "Human":
    print("You won!")
elif move == "Computer":
    print("Sorry, you've lost. Better luck next time..")

