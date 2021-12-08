# -*- coding: utf-8 -*-
"""
@author: WSJHawkins
"""

import ingeniousHelper
import ingeniousStrategies
import numpy as np
import math
import random
import colorama
colorama.init(strip=False)

    
bestVars = [0,0,0,0,0,0,0,0]
bestPercent = 0
for z in range(0,1):
    winner = [0,0]
    numOfGames = 50
    viewGame = False
    gameOver = 0
    var1 = random.randint(0,100)/10
    var2 = random.randint(0,100)/10
    var3 = random.randint(0,100)/10
    var4 = random.randint(0,100)/10
    var5 = random.randint(0,100)/10
    var6 = random.randint(0,100)/10
    var7 = random.randint(0,100)/10
    var8 = random.randint(0,100)/10
    randomVars = [var1,var2,var3,var4,var5,var6,var7,var8]
    for k in range(0,8):
        if(randomVars[k] == 0):
            randomVars[k] = 0.01
    for n in range(numOfGames):
        #Initialise Game
        numOfPlayers = 2 
        board = createBoard(numOfPlayers)
        
        #Initialise Tile Bag
        tileBag = fillTileBag()
        
        #Player 1
        scoreBoard = [0,0,0,0,0,0]
        tileRack,tileBag = generateTileRack(tileBag)
    
        #Player2
        scoreBoard2 = [0,0,0,0,0,0]
        tileRack2,tileBag = generateTileRack(tileBag)
        #Print Game State
        if(viewGame):
            printGameState(board,tileRack,scoreBoard,2)
               
        #Start Game
        for i in range(0,1000):
            if(viewGame):
                input('Press ENTER to continue...')
            
            #Player1
            anotherGo = 1
            while(anotherGo == 1):
                board,scoreBoard,tileRack,tileBag,gameOver,anotherGo = playTurnComputer(board,scoreBoard,scoreBoard2,tileRack,tileBag,i,9,randomVars)
                if(viewGame and gameOver == 0):
                    print("Player 1")
                    printGameState(board,tileRack,scoreBoard,1)
            if(gameOver==1):
                break
            
            if(viewGame):
                input('Press ENTER to continue...')
            
            #Player2
            anotherGo = 1
            while(anotherGo == 1):
                board,scoreBoard2,tileRack2,tileBag,gameOver,anotherGo = playTurnComputer(board,scoreBoard2,scoreBoard,tileRack2,tileBag,i,0,randomVars)     
                #board,scoreBoard2,tileRack2,tileBag,gameOver,anotherGo = playTurnHuman(board,scoreBoard2,scoreBoard,tileRack2,tileBag,i,numOfPlayers,8,randomVars)     
                if(viewGame and gameOver == 0):
                    print("Player 2")
                    printGameState(board,tileRack2,scoreBoard2,1)
            if(gameOver==1):
                break   
           
        if(viewGame): 
            print("Game Over")
            printGameState(board,tileRack,scoreBoard,1)
            printGameState(board,tileRack2,scoreBoard2,3)
        
        #Who Won   
        scoreBoard.sort()
        scoreBoard2.sort()
        if(scoreBoard>scoreBoard2):
            winner[0] = winner[0] + 1
            #print("Player 1 Won Game: "+str(n)+ " so far: "+str(winner[0]))
        else:
            winner[1] = winner[1] + 1
            #print("Player 2 Won Game: "+str(n)+ " so far: "+str(winner[1]))
    
    percentage = winner[0]/numOfGames * 100
    percentage = round(percentage,1)
    print("Player 1 Won "+str(percentage)+"% Of The "+str(numOfGames)+" Games")
    if(percentage >= 70):
        bestVars[0] = var1
        bestVars[1] = var2
        bestVars[2] = var3
        bestVars[3] = var4
        bestVars[4] = var5
        bestVars[5] = var6
        bestVars[6] = var7
        bestVars[7] = var8
        print(percentage)
        print(bestVars[0])
        print(bestVars[1])
        print(bestVars[2])
        print(bestVars[3])
        print(bestVars[4])
        print(bestVars[5])
        print(bestVars[6])
        print(bestVars[7])
        print()

print(bestVars[0])
print(bestVars[1])
print(bestVars[2])
print(bestVars[3])
print(bestVars[4])
print(bestVars[5])
print(bestVars[6])
print(bestVars[7])
    