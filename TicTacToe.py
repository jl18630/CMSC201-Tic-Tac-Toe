#File: proj1.py                                                                
#Name: Kyle Lee                                                                 
#Date: April 12 2016                                                          
#Lab Section: 22                                                              
#Email: leek4@umbc.edu                                                         
#Description: This python program allows two players to play Tic-Tac-Toe. The p\rogram begins with a random player and symbol every time the game is played. Bo\th players have the option to save the game and load the saved game and continue playing the loaded game. If a winner is found, the winner has the choice to restart another game or end.                                                     
import random

#drawBoard() draws the board with numbers 1-9 at the beginning of the game. Whe\n players input a  number, the board will update with the player's symbol.      
#Outuput: return lists                                                         
#Side-effects: none                                                             
def drawBoard(listRow1, listRow2, listRow3):
#Append numbers 1-9 to appropriate row                                          
    for i in range(1, 4):
        listRow1.append(str(i))
    for i in range(4, 7):
        listRow2.append(str(i))
    for i in range (7, 10):
        listRow3.append(str(i))

    print(listRow1[0] + "|" + listRow1[1] + "|" + listRow1[2])
    print("-----")
    print(listRow2[0] + "|" + listRow2[1] + "|" + listRow2[2])
    print("-----")
    print(listRow3[0] + "|" + listRow3[1] + "|" + listRow3[2])
    print("\n")

    return listRow1, listRow2, listRow3

#updateBoard() changes the number on the board to the player's symbol, and prin\
ts out an updated board                                                         
#Input: input number, row 1, row 2, row 3 contents as arguments                
#Output: returns updated row 1, row2, row 3, and validation to switch players  
#Side-effects: none                                                             
def updateBoard(inputMark, symbol, listRow1, listRow2, listRow3):
    changePlayers = False

#If the input number is 1-9                                                     
    if(inputMark == "1"):
#If the spot of the input number is already filled                              
        if(listRow1[0] == "X" or listRow1[0] == "O"):
#Keep symbol in the spot                                                        
            print("That space is already taken.")
            listRow1[0] = listRow1[0]
        else:
#If the spot has no symbol, change the number with the players symbol           
            listRow1[0] = symbol
            changePlayers = True
        
#Repeats steps for all numbers up to 9                                          
    if(inputMark == "2"):
        if(listRow1[1] == "X" or listRow1[1] == "O"):
            print("That space is already taken.")
            listRow1[1] = listRow1[1]
        else:
            listRow1[1] = symbol
            changePlayers = True
    if(inputMark == "3"):
        if(listRow1[2] == "X" or listRow1[2] == "O"):
            print("That space is already taken.")
            listRow1[2] = listRow1[2]
        else:
            listRow1[2] = symbol
            changePlayers = True
    if(inputMark == "4"):
        if(listRow2[0] == "X" or listRow2[0] == "O"):
            print("That space is already taken.")
            listRow2[0] = listRow2[0]
        else:
            listRow2[0] = symbol
            changePlayers = True
    if(inputMark == "5"):
        if(listRow2[1] == "X" or listRow2[1] == "O"):
            print("That space is already taken.")
            listRow2[1] = listRow2[1]
        else:
            listRow2[1] = symbol
            changePlayers = True
    if(inputMark == "6"):
        if(listRow2[2] == "X" or listRow2[2] == "O"):
            print("That space is already taken.")
            listRow2[2] = listRow2[2]
        else:
            listRow2[2] = symbol
            changePlayers = True
    if(inputMark == "7"):
        if(listRow3[0] == "X" or listRow3[0] == "O"):
            print("That space is already taken.")
            listRow3[0] = listRow3[0]
        else:
            listRow3[0] = symbol
            changePlayers = True
    if(inputMark == "8"):
        if(listRow3[1] == "X" or listRow3[1] == "O"):
            print("That space is already taken.")
            listRow3[1] = listRow3[1]
        else:
            listRow3[1] = symbol
            changePlayers = True
    if(inputMark == "9"):
        if(listRow3[2] == "X" or listRow3[2] == "O"):
            print("That space is already taken.")
            listRow3[2] = listRow3[2]
        else:
            listRow3[2] = symbol
            changePlayers = True

            #Draws board with the symbol filled                                             
    if(inputMark != "-2"):
        draw = drawBoard(listRow1, listRow2, listRow3)

    return listRow1, listRow2, listRow3, changePlayers


#saveGame() saves the game with the current player, symbol, and board          
#Input: player, symbol, row 1, row 2, row3 as arguments                        
#Output: return stop                                                            
#Side-effects: none                                                             
def saveGame(player, symbol, listRow1, listRow2, listRow3):
#stop allows the game to be paused and asks the player if they wish to restart \
or end. If the player says no, then the game will end.                          
    stop = False

    openFile = open("tic.txt", "w")
    dataFile = openFile

#Saves each row with its contents into a text file                              
    saveFile = dataFile.write(listRow1[0] + listRow1[1] + listRow1[2] + ";")
    saveFile = dataFile.write(listRow2[0] + listRow2[1] + listRow2[2] + ";")
    saveFile = dataFile.write(listRow3[0] + listRow3[1] + listRow3[2] + ";")
#Saves player number into a text file                                           
    saveFile = dataFile.write(player + ";")
#Saves symbol into a text file                                                  
    saveFile = dataFile.write(symbol)

    print("File Saved")

#Asks the player if they wish to restart or end the game                        
    startOver = winOrRepeat()
    if(startOver == True):
        restartGame = main()

    stop = True
    dataFile.close()

    return stop

#loadGame() loads in the saved contents from the text file and updates the boar\
d with the loaded content                                                       
#Input: none                                                                    
#Output: returns loaded row 1, row 2, row 3, player, and symbol                 
#Side-effects: none                                                             
def loadGame():
    player = []
    symbol = []
    loadListRow1 = []
    loadListRow2 = []
    loadListRow3 = []

    loadGame = False

    openFile = open("tic.txt")
    dataFile = openFile

#For each string in the text file                                               
    for i in dataFile:
#Separate each element in a list                                                
        readFile = i.strip()
        readFile = i.split(";")
        row1, row2, row3, player, symbol = readFile

#Separate the row 1, row 2, and row 3 strings with individual characters        
    for i in row1:
        loadListRow1.append(i)
    for i in row2:
        loadListRow2.append(i)
    for i in row3:
        loadListRow3.append(i)

    print(row1[0] + "|" + row1[1] + "|" + row1[2])
    print("-----")
    print(row2[0] + "|" + row2[1] + "|" + row2[2])
    print("-----")
    print(row3[0] + "|" + row3[1] + "|" + row3[2])

    print("Loaded Game \n")
    loadGame = True
    dataFile.close()

    return loadGame, loadListRow1, loadListRow2, loadListRow3, player, symbol

#playerCount() randomizes the player at the beginning of the game               
#Input: none                                                                    
#Output: returns player number (1 or 2)                                         
#Side-effects: none                                                             
def playerCount():
    player = random.randint(1,2)
    if(player == 1):
        player = "1"
    elif(player == 2):
        player = "2"

    return player

#symbolCount randomizes the symbol at the beginning of the game                 
#Input: none                                                                    
#Output: returns symbol (X or O)                                                
#Side-effects: none                                                             
def symbolCount():
    symbol = random.randint(1,2)
    if(symbol == 1):
        symbol = "X"
    elif(symbol == 2):
        symbol = "O"

    return symbol

#markBoard() asks the user a number (1-9) to fill with player 1's or 2's symbol
#Input: number (1-9) to fill with symbol. Player number as argument             
#Output: returns the input number                                               
#Side-effects: none                                                             
def markBoard(player):
    validation = False

    while(validation == False):
#Asks current player to input number                                            
        print("Player", player, "what is your choice?")
        inputMark = str(input("(1-9) or -1 to save or -2 to load: "))
#If number is between 1-9 while loop stops                                      
        if(inputMark >= "1" and inputMark <= "9"):
            validation = True
#If number is -1 save the game and while loop stops                             
        elif(inputMark == "-1"):
            validation = True
#If number is -2 load the game and while loop stops                             
        elif(inputMark == "-2"):
            validation = True
        else:
            print("Invalid choice")

    return inputMark

#switch() switches between player 1 and 2 along with their symbols after each t\
urn                                                                             
#Input: current player and symbol as arguments                                  
#Output: return switched player and symbol                                      
#Side-effects: none                                                             
def switch(player, symbol):
    if(player == "1"):
        player = "2"
    elif(player == "2"):
        player = "1"
    if(symbol == "X"):
        symbol = "O"
    elif(symbol == "O"):
        symbol = "X"

    return player, symbol

#winning() checks to see if there are any symbols three in a row horizantally, \
vertically, or diagonally. If there is no winner when all numbers are filled, then it is a tie                                                                 
#Input: current player and symbol, row 1, row 2, row 3 contents as arguements   
#Output: returns validation to restart or end game                              
def winning(player, symbol, listRow1, listRow2, listRow3):
    validation = False

    #Checks for three marks in a row horizantally                              \
                                                                                
    if(listRow1[0] == listRow1[1] and listRow1[1] == listRow1[2]):
        print("Player", player, "is the winner!")
        validation = True
    elif(listRow2[0] == listRow2[1] and listRow2[1] == listRow2[2]):
        print("Player", player, "is the winner!")
        validation = True
    elif(listRow3[0] == listRow3[1] and listRow2[1] == listRow3[2]):
        print("Player", player, "is the winner!")
        validation = True
#Checks for three marks in a row vertically  
    elif(listRow1[0] == listRow2[0] and listRow2[0] == listRow3[0]):
        print("Player", player, "is the winner!")
        validation = True
    elif(listRow1[1] == listRow2[1] and listRow2[1] == listRow3[1]):
         print("Player", player, "is the winner!")
         validation = True
    elif(listRow1[2] == listRow2[2] and listRow2[2] == listRow3[2]):
         print("Player", player, "is the winner!")
    #Checks for three marks in a row diagonally      
                                                                                
    elif(listRow1[0] == listRow2[1] and listRow2[1] == listRow3[2]):
         print("Player", player, "is the winner!")
         validation = True
    elif(listRow1[2] == listRow2[1] and listRow2[1] == listRow3[0]):
         print("Player", player, "is the winner!")
         validation = True
    #If there are no winner and all positions are filled, then it is a tie      
    else:
        if((listRow1[0] == "X" or listRow1[0] == "O") and (listRow1[1] == "X" or listRow1[1] == "O") and (listRow1[2] == "X" or listRow1[2] == "O") and (listRow2[0] == "X" or listRow2[0] == "O") and (listRow2[1] == "X" or listRow2[1] == "O") and (listRow2[2] == "X" or listRow2[2] == "O") and (listRow3[0] == "X" or listRow3[0] == "O") and (listRow3[1] == "X" or listRow3[1] == "O") and (listRow3[2] == "X" or listRow3[2] == "O")):
            print("Tie!")
            validation = True

    return validation

#winOrRepeat() asks the winner if he/she wishes to restart the game with a clea\
n board or end the game                                                         
#Input: yes or no                                                               
#Output: returns validationContinue to restart game (if yes)                    
#Side-effects: none                                                             
def winOrRepeat():
    validationContinue = False
    validation = False

#Ask player is he/she wishes to restart or end game. Keeps asking player until \
providing a valid response.                                                     
    while(validation == False):
        inputRepeat = str(input("Play again?: "))
        if(inputRepeat.upper() == "NO" or inputRepeat.upper() == "N"):
            print("Thank you for playing")
            validation = True
        elif(inputRepeat.upper() == "YES" or inputRepeat.upper() == "Y"):
            validationContinue = True
            validation = True
        else:
            print("Invalid choice")
    print("\n")

    return validationContinue

#main() calls the functions to form Tic-Tac-Toe and operates the logic of turns\
 between player 1 and 2                                                         
#Input: none                                                                    
#Output: none                                                                   
#Side-effects: none                                                             
def main():
    listRow1 = []
    listRow2 = []
    listRow3 = []

    keepPlayingGame = True
    useStartOverFunction = True
    load = False
    loadedGame = False
    keepGoing= False
    turn = "0"

    print("Welcome to Tic-Tac-Toe\nThis is for two players")

#Initalizes starting player and symbol                                          
    player = playerCount()
    symbol = symbolCount()

    print("Player", player, "will go first and will play with the", symbol)

#FIRST PLAYER'S TURN                                                            
    row1, row2, row3 = drawBoard(listRow1, listRow2, listRow3)
    mark = markBoard(player)
    updateListRow1, updateListRow2, updateListRow3, changePlayers = updateBoard(mark, symbol, row1, row2, row3)

    if(mark == "-1"):
        save = saveGame(player, symbol, row1, row2, row3)
        #If player says 'yes'                                                   
        if(save == True):
            #Restart game                                                       
            restartGame = replayGame()
    elif(mark == "-2"):
        #Load contents into game from text file                                 
        load, loadRow1, loadRow2, loadRow3, loadPlayer, loadSymbol = loadGame()
        keepPlayingGame = False
        loadedGame = True
    else:
        #Go to next turn                                                        
        turn = "1"

    while(keepPlayingGame == True):
#SECOND PLAYER'S TURN                                                           
        if(turn == "1"):
            switchPlayer, switchSymbol = switch(player, symbol)
            mark = markBoard(switchPlayer)

            if(mark == "-1"):
                save = saveGame(switchPlayer, switchSymbol, updateListRow1, updateListRow2, updateListRow3)
                if(save == True):
                    useStartOverFunction = False
                    keepPlayingGame = False
            elif(mark == "-2"):
                load, loadRow1, loadRow2, loadRow3, loadPlayer, loadSymbol = loadGame()
                if(load == True):
                    loadedGame = True
                    keepPlayingGame = False

            #If player inputs any number from 1-9                               
            if(useStartOverFunction == True):
                #Update board with position being marked by player's symbol updateNewListRow1, updateNewListRow2, updateNewListRow3, changePlayers = updateBoard(mark, switchSymbol, updateListRow1, updateListRow2, updateListRow3)
                #If player marks a position that has not been already filled    
                if(changePlayers == True):
                    #switch to next player                                      
                    switchNewPlayer, switchNewSymbol = switch(switchPlayer, switchSymbol)
                    turn = "0"
                #If player picks an already filled spot                         
                elif(changePlayers == False):
                    #Do not switch player until picking a position that has not been filled                                     
                    turn = "1"

#RETURNS BACK TO FIRST PLAYER'S TURN (SAME CODING FORMAT AS ABOVE)              
        elif(turn == "0"):
            mark = markBoard(player)
            if(mark == "-1"):
                save = saveGame(switchNewPlayer, switchNewSymbol, updateListRow1, updateListRow2, updateListRow3)
                if(save == True):
                    useStartOverFunction = False
                    keepPlayingGame = False
            elif(mark == "-2"):
                load, loadRow1, loadRow2, loadRow3, loadPlayer, loadSymbol = loadGame()
                if(load == True):
                    loadedGame = True
                    keepPlayingGame = False
            if(useStartOverFunction == True):
                updateListRow1, updateListRow2, updateListRow3, changePlayers = updateBoard(mark, symbol, row1, row2, row3)
                if(changePlayers == True):
                    switchPlayer, switchSymbol = switch(switchPlayer, switchSymbol)
                    turn = "1"
                elif(changePlayers == False):
                    turn = "0"

        #Checks for a winner after each turn                                    
        winner = winning(switchPlayer, switchSymbol, updateListRow1, updateListRow2, updateListRow3)
        #If a winner is found stop while loop (goes to the bottom of main() and calls winOrRepeat())                                                           
        if(winner == True):
            keepPlayingGame = False


#IF A GAME IS LOADED, PROGRAM GOES TO THIS WHILE LOOP TO PLAY LOADED GAME       
    while(loadedGame == True):

#PLAYER 1                                                                       
        if(loadPlayer == "1"):
            #Ask player to mark board                                           
            mark = markBoard(loadPlayer)

            if(mark == "-1"):
                save = saveGame()
                if(save == True):
                    useStartOverFunction = False
                    loadedGame = False
            elif(mark == "-2"):
                load, loadRow1, loadRow2, loadRow3, loadPlayer, loadSymbol = loadGame()
                if(load == True):
                    loadedGame = True

            #In the first turn after loading game                               
            if(useStartOverFunction == True and keepGoing == False):
                #update board for the first turn                                
                updateLoadRow1, updateLoadRow2, updateLoadRow3, changePlayers = updateBoard(mark, loadSymbol, loadRow1, loadRow2, loadRow3)
            #In turns after the first turn (to allow the board to continuously updated)                                                                        
            elif(useStartOverFunction == True and keepGoing == True):
                #update board for turns after the first turn                    
                updateLoadRow1, updateLoadRow2, updateLoadRow3, changePlayers = updateBoard(mark, switchSymbol, updateLoadRow1, updateLoadRow2, updateLoadRow3)

            #In the first turn after loading game                               
            if(changePlayers == True):
                switchPlayer, switchSymbol = switch(loadPlayer, loadSymbol)
                loadPlayer = "2"
                keepGoing = True
            #In turns after the first turn                                      
            elif(changePlayers == True and keepGoing == True):
                switchPlayer, switchSymbol = switch(switchPlayer, switchSymbol)
                loadPlayer = "2"
            elif(changePlayers == False):
                loadPlayer = "1"

            #Player 2 (SAME CODING FORMAT AS ABOVE)                                         
        elif(loadPlayer == "2"):
            mark = markBoard(loadPlayer)

            if(mark == "-1"):
                save = saveGame()
                if(save == True):
                    useStartOverFunction = False
                    loadedGame = False
            elif(mark == "-2"):
                load, loadRow1, loadRow2, loadRow3, loadPlayer, loadSymbol = loadGame()
                if(load == True):
                    loadedGame = True

            if(useStartOverFunction == True and keepGoing == False):
                updateLoadRow1, updateLoadRow2, updateLoadRow3, changePlayers = updateBoard(mark, loadSymbol, loadRow1, loadRow2, loadRow3)
            elif(useStartOverFunction == True and keepGoing == True):
                updateLoadRow1, updateLoadRow2, updateLoadRow3, changePlayers = updateBoard(mark, switchSymbol, updateLoadRow1, updateLoadRow2, updateLoadRow3)
        
                    if(changePlayers == True and keepGoing == False):
                switchPlayer, switchSymbol = switch(loadPlayer, loadSymbol)
                loadPlayer = "1"
                keepGoing = True
            elif(changePlayers == True and keepGoing == True):
                switchPlayer, switchSymbol = switch(switchPlayer, switchSymbol)
                loadPlayer = "1"
            elif(changePlayers == False):
                loadPlayer = "2"

        #Checks for winner after each turn                                      
        winner = winning(loadPlayer, loadSymbol, updateLoadRow1, updateLoadRow2, updateLoadRow3)
        #If winner is found stop while loop                                     
        if(winner == True):
            loadedGame = False
    
      #After a regular or loaded game is completed with a winner found            
    if(useStartOverFunction == True):
        startOver = winOrRepeat()
        #If winner says 'yes'                                                   
        if(startOver == True):
            #Restart game                                                       
            restartGame = main()

main()


