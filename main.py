play=True
RED_CIRCLE = '\033[91m●\033[0m'      # Red circle
YELLOW_CIRCLE = '\033[93m●\033[0m'   # Yellow circle

# Define the function drawField that will print the game field
def drawField(field):
    for row in range(6):
        practicalRow = int(row)
        for column in range(15):
            if column%2 == 1:
                practicalColumn = int(column/2)
                if column != 15:
                    print(field[practicalColumn][practicalRow],end="")
                else:
                    print(field[practicalColumn][practicalRow])
            else:
                print("|", end="")     
        print("")

# Condensing Repeated Code To A Single Function 
def winner(field, col, row):
    if field[col][row] == RED_CIRCLE:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

#Check if there is a winner or draw
def gameEnd(field):
    # Check for tie (board is full)
    board_full = True
    for col in range(7):
        for row in range(6):
            if field[col][row] == " ":
                board_full = False
                break
        if not board_full:
            break
    
    if board_full:
        print("It's a tie!")
        return False

    # Check vertical wins (columns)
    for col in range(7):
        for row in range(3):
            if (field[col][row] == field[col][row + 1] == field[col][row + 2] == field[col][row + 3] != " "):
                winner(field, col, row)
                return False
    
    # # Check horizontal wins (rows)
    for col in range(4):
        for row in range(6):
            if(field[col][row] == field[col + 1][row] == field[col + 2][row] == field[col + 3][row] != " "):
                winner(field, col, row)
                return False
    
    # Check diagonal wins
    # Top-left to bottom-right
    for col in range(4):
        for row in range(3):
            if(field[col][row] == field[col + 1][row + 1] == field[col + 2][row + 2] == field[col + 3][row + 3] != " "):
                winner(field, col, row)
                return False
    
    # Top-right to bottom-left
    for col in range(3, 7):
        for row in range(3):
            if(field[col][row] == field[col - 1][row + 1] == field[col - 2][row + 2] == field[col - 3][row + 3] != " "):
                winner(field, col, row)
                return False
    
    # Game continues
    return True

# #Place Player's piece at the lowest point possible. 
def movePiece(player, field, col):
    if col < 0 or col > 6:
        print("Invalid Column Selection. Please Enter 1-7")
        return field, False

    if field[col][0] != " ":
        print("Column Is Full. Try Again.")
        return field, False

    i = 5
    while i >= 0:
        if field[col][i] == " ":
            if player == 1:
                field[col][i] = RED_CIRCLE
            else:
                field[col][i] = YELLOW_CIRCLE
            return field, True
        i -= 1
     
    return field, False
        


# Create a variable for the Players
Player = 1

# Create a list with each element corresponds to a column
# A list that contains 7 lists
currentField = [
    [" ", " ", " ", " ", " ", " "], 
    [" ", " ", " ", " ", " ", " "], 
    [" ", " ", " ", " ", " ", " "], 
    [" ", " ", " ", " ", " ", " "], 
    [" ", " ", " ", " ", " ", " "], 
    [" ", " ", " ", " ", " ", " "], 
    [" ", " ", " ", " ", " ", " "]
]

# We will draw the current field
drawField(currentField)

# Create an infinite loop for the game
while(play == True):
    # Display the player's turn
    print("Players turn: ",Player)
    
    # Ask user for input: to specify the desired row and column
    MoveColumn = int(input("Please enter the column: ")) - 1 # Convert the column to integer
    
    # Validate Player's Move
    currentField, move_successful = movePiece(Player, currentField, MoveColumn)
    if move_successful:
        if Player == 1:
            Player = 2
        else:
            Player = 1

    # Check if there is a winner or a draw
    play = gameEnd(currentField)

    # At the end, draw the current field representation
    drawField(currentField)
