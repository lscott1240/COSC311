def runGame():
    # Function for printing board
    def printBoard():
        for i in row0:
            print(i, end = ' ')
        print("\n", bar)
        for i in row1:
            print(i, end = ' ')
        print("\n", bar)
        for i in row2:
            print(i, end = ' ')
            
    # Function for checking winner
    def checkGame():
        winner = ' '
        
        # Check rows for winner
        if (row0[0] == row0[4] and row0[0] == row0[8] and row0[0] != ' '):
            winner = row0[0]
        if (row1[0] == row1[4] and row1[0] == row1[8] and row1[0] != ' '):
            winner = row1[0]
        if (row2[0] == row2[4] and row2[0] == row2[8] and row2[0] != ' '):
            winner = row2[0]
        
        # Check columns for winner
        if (row0[0] == row1[0] and row0[0] == row2[0] and row0[0] != ' '):
            winner = row0[0]
        if (row0[4] == row1[4] and row0[4] == row2[4] and row0[4] != ' '):
            winner = row0[4]
        if (row0[8] == row1[8] and row0[8] == row2[8] and row0[8] != ' '):
            winner = row0[8]
            
        # Check diagonals for winner
        if (row0[0] == row1[4] and row0[0] == row2[8] and row0[0] != ' '):
            winner = row0[0]
        if (row2[0] == row1[4] and row2[0] == row0[8] and row2[0] != ' '):
            winner = row2[0]
            
        return winner
       
    # Check for valid row/column input 
    def checkInput(player_input):
        
        if (player_input < 0 or player_input > 2):
            print("Invalid input")
            return False
        else:
            return True
    
    # Check move to avoid overwriting previous move's
    def checkBlock(row, column):
        
        if (row == 0):
            if (row0[column * 4] != ' '):
                return False
        elif (row == 1):
            if (row1[column * 4] != ' '):
                return False
        elif (row == 2):
            if (row2[column * 4] != ' '):
                return False
        else:
            return True
    
    # Plays move in correct position
    def playMove(row, column, player):
        
        if (row == 0):
            row0[column * 4] = player
        if (row == 1):
            row1[column * 4] = player
        if (row == 2):
            row2[column * 4] = player
    
    # Establish User Interface
    row0 = [' ',' ','|',' ',' ',' ','|',' ',' ']
    row1 = [' ',' ','|',' ',' ',' ','|',' ',' ']
    row2 = [' ',' ','|',' ',' ',' ','|',' ',' ']
    bar = '---------------'
        
    row_input = -1
    column_input = -1
    # Run the game
    for i in range(0,9):
        
        # Print Board
        printBoard()
        
        # Check Player Turn
        if (i % 2 == 0):
            print("\n\nX player's turn:\n")
        else:
            print("\n\nO player's turn:\n'")
 
        # Create inputs for error checking input
        check = False
        while (check == False):
            row_input = int(input("Enter a valid row for move ( 0 - 2 ) : "))
            column_input = int(input("Enter a valid column for move ( 0 - 2 ) : "))
            check = checkBlock(row_input, column_input)
            if (checkInput(row_input) == False or checkInput(column_input) == False):
                print("Invalid Input")
                check = False
            elif (check == False):
                print("Invalid Move")
        
        # Check Player Turn for successful Move
        if (i % 2 == 0):
            playMove(row_input, column_input, 'X')
        else:
            playMove(row_input, column_input, 'O')
        
        # Check for Win
        check_win = checkGame()
        if (check_win != ' '):
            break
        
    # Print Results
    printBoard()
    if (check_win == ' '):
        print("\nIt's a tie!")
    else:
        print("\nCongratulations, player", check_win, "wins!")
    
player_play = input("Would you like to play tic tac toe? (enter 'yes' or 'no') ") 

while(player_play == 'yes'):
    runGame()
    player_play = input("Would you like to play again? (enter 'yes' or 'no') ")
