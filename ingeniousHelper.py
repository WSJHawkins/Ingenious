# -*- coding: utf-8 -*-
"""
@author: WSJHawkins
"""

from ingeniousStrategies import *
import math
import colorama
import numpy as np
from numpy.random import randint


def numToColour(x):
    returnVal = ""
    if x == 1:
        returnVal = colorama.Fore.RED + colorama.Style.BRIGHT
    elif x == 2:
        returnVal = colorama.Fore.GREEN + colorama.Style.BRIGHT
    elif x == 3:
        returnVal = colorama.Fore.MAGENTA + colorama.Style.BRIGHT
    elif x == 4:
        returnVal = colorama.Fore.BLUE + colorama.Style.BRIGHT
    elif x == 5:
        returnVal = colorama.Fore.YELLOW + colorama.Style.BRIGHT
    elif x == 6:
        returnVal = '\033[33m'
    else:
        returnVal = colorama.Fore.BLACK

    return returnVal


def createBoard(numOfPlayers):
    board = np.zeros((15, 15), dtype=int)
    maxWidth = 15 - (4 - numOfPlayers) * 2
    for j in range(15):
        width = j + 2 * numOfPlayers
        if width > maxWidth:
            width = (maxWidth * 2) - width
        for i in range(15):
            if j < (4 - numOfPlayers) or j > (15 - (4 - numOfPlayers) - 1):
                board[j][i] = -1
            elif i < (4 - numOfPlayers) or i > (15 - (4 - numOfPlayers) - 1):
                board[j][i] = -1
            elif i > ((4 - numOfPlayers) + width - 1):
                board[j][i] = -1

    board[2][2] = 1
    board[2][7] = 2
    board[7][2] = 3
    board[7][12] = 4
    board[12][2] = 5
    board[12][7] = 6
    return board


def printBoard(board):
    for j in range(15):
        print()
        count = 0

        for i in range(15):
            if board[j][i] == -1:
                count = count + 1

        for k in range(math.floor(count / 2)):
            print(" .", end='')
            if k != math.floor(count / 2) - 1:
                print(" ", end='')
            if ((j % 2) != 1) and (k == math.floor(count / 2) - 1):
                print(" ", end='')

        for i in range(15):
            if board[j][i] != -1:
                print(" ", end='')
                print(numToColour(board[j][i]) + str(board[j][i]) + colorama.Style.RESET_ALL, end='')
                print(" ", end='')

        for k in range(math.ceil(count / 2)):
            print(" . ", end='')
    print()


def fillTileBag():
    tileBag = []
    # 5 of each double
    for i in range(1, 7):
        for j in range(0, 5):
            tileBag.append([i, i])

    # 6 of each pair
    for i in range(1, 6):
        for j in range(i + 1, 7):
            if i != j:
                for k in range(0, 6):
                    tileBag.append([i, j])
    return tileBag


def printTileRack(tileRack):
    print(tileRack[0][0], "  ", tileRack[1][0], "  ", tileRack[2][0], "  ", tileRack[3][0], "  ", tileRack[4][0], "  ",
          tileRack[5][0])
    print(tileRack[0][1], "  ", tileRack[1][1], "  ", tileRack[2][1], "  ", tileRack[3][1], "  ", tileRack[4][1], "  ",
          tileRack[5][1])


def printScoreBoard(scoreBoard):
    print()
    print("---------------------------------------------------------------")
    print("|   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 |")
    for j in range(1, 7):
        print('|' + numToColour(j) + str(j) + '  ', end='')
        for i in range(scoreBoard[j - 1]):
            print('.  ', end='')
        print('x  ', end='')
        for i in range(18 - scoreBoard[j - 1]):
            print('.  ', end='')
        print(colorama.Style.RESET_ALL + '|')
    print("---------------------------------------------------------------")
    print()


def printGameState(board, tileRack, scoreBoard, method):
    if method == 0:
        printBoard(board)
        printScoreBoard(scoreBoard)
        printTileRack(tileRack)
    if method == 1:
        printBoard(board)
        printScoreBoard(scoreBoard)
    if method == 2:
        printBoard(board)
    if method == 3:
        printScoreBoard(scoreBoard)


def availablePlaces(j, i, board):
    placeList = []
    if j < 7:
        placeList = [[j + 1, i + 1], [j, i + 1], [j + 1, i], [j - 1, i], [j, i - 1], [j - 1, i - 1]]
    elif j == 7:
        placeList = [[j + 1, i - 1], [j, i + 1], [j + 1, i], [j - 1, i], [j, i - 1], [j - 1, i - 1]]
    elif j > 7:
        placeList = [[j + 1, i - 1], [j, i + 1], [j + 1, i], [j - 1, i], [j, i - 1], [j - 1, i + 1]]
    if board[j][i] != 0:
        placeList = []
    placeList2 = []
    for x in placeList:
        if 15 > x[0] >= 0 >= 0 and x[1] < 15:
            if board[x[0]][x[1]] == 0:
                placeList2.append(x)
    return placeList2


def nextDoorPieces(j, i, board):
    placeList = []
    if j < 7:
        placeList = [[j + 1, i + 1], [j, i + 1], [j + 1, i], [j - 1, i], [j, i - 1], [j - 1, i - 1]]
    elif j == 7:
        placeList = [[j + 1, i - 1], [j, i + 1], [j + 1, i], [j - 1, i], [j, i - 1], [j - 1, i - 1]]
    elif j > 7:
        placeList = [[j + 1, i - 1], [j, i + 1], [j + 1, i], [j - 1, i], [j, i - 1], [j - 1, i + 1]]
    if board[j][i] != 0:
        placeList = []
    placeList2 = []
    for x in placeList:
        if 0 <= x[0] < 15 and 0 <= x[1] < 15:
            if board[x[0]][x[1]] > 0:
                placeList2.append(x)
    return placeList2


def generateTileRack(tileBag):
    tileRack = []
    for i in range(0, 6):
        tileNo = randint(0, len(tileBag) - 1)
        tileRack.append(tileBag[tileNo])
        tileBag.remove(tileBag[tileNo])
    return tileRack, tileBag


def refreshTileRack(tileRack, tileBag):
    for i in tileRack:
        if i[0] == -1:
            tileNo = randint(0, len(tileBag) - 1)
            i[0] = tileBag[tileNo][0]
            i[1] = tileBag[tileNo][1]
            tileBag.remove(tileBag[tileNo])
    return tileRack, tileBag


def incrementScore(score, tileNum):
    if score[1][tileNum] < 18:
        score[0] = score[0] + 1
        score[1][tileNum] += 1
    return score


def scoreLine(board, location, n, score):
    if location[0] == n[0]:
        # going side to side
        tmp = location[1]
        location[1] = n[1]
        n[1] = n[1] + n[1] - tmp
        if 0 <= n[0] < 15 and 0 <= n[1] < 15:
            if board[location[0]][location[1]] == board[n[0]][n[1]]:
                score = incrementScore(score, board[n[0]][n[1]] - 1)
                score = scoreLine(board, location, n, score)
    else:
        # diaganol
        incrementI = n[1] - location[1]
        if n[0] == 7:
            if incrementI == 0:
                incrementI = 1
            else:
                incrementI = 0
        location[1] = n[1]
        n[1] = n[1] + incrementI
        tmp = location[0]
        location[0] = n[0]
        n[0] = n[0] + n[0] - tmp
        if 0 <= n[0] < 15 and 0 <= n[1] < 15:
            if board[location[0]][location[1]] == board[n[0]][n[1]]:
                score = incrementScore(score, board[n[0]][n[1]] - 1)
                score = scoreLine(board, location, n, score)

    return score


def scoreMove(location, position, tile, board, scoreBoard):
    total = 0
    for score in scoreBoard:
        total = total + score
    score = [total, [scoreBoard[0], scoreBoard[1], scoreBoard[2], scoreBoard[3], scoreBoard[4], scoreBoard[5]]]

    for n in nextDoorPieces(location[0], location[1], board):
        if n[0] != position[0] or n[1] != position[1]:
            if tile[0] == board[n[0]][n[1]]:
                score = incrementScore(score, tile[0] - 1)
                # then look at line
                score = scoreLine(board, location[:], n[:], score[:])

    for n in nextDoorPieces(position[0], position[1], board):
        if n[0] != location[0] or n[1] != location[1]:
            if tile[1] == board[n[0]][n[1]]:
                score = incrementScore(score, tile[1] - 1)
                # then look at line
                score = scoreLine(board, position[:], n[:], score[:])
    return score


def setScoreBoard(maxScore, scoreBoard):
    scoreBoard = maxScore[:]
    return scoreBoard


def removeTileFromRack(tileRack, tile):
    for t in tileRack:
        if t[0] == tile[0] and t[1] == tile[1]:
            t[0] = -1
            t[1] = -1
            break
    return tileRack


def placeTile(board, bestLocation):
    board[bestLocation[0][0]][bestLocation[0][1]] = bestLocation[2][0]
    board[bestLocation[1][0]][bestLocation[1][1]] = bestLocation[2][1]
    return board


def playTurnComputer(board, scoreBoard, otherScoreBoard, tileRack, tileBag, turnNo, method, randomVars):
    gameOver = 1
    anotherGo = 0
    bestLocation = []
    score = [0, [0, 0, 0, 0, 0, 0]]
    maxScore = [0, [0, 0, 0, 0, 0, 0]]

    for j in range(15):
        for i in range(15):
            location = [j, i]
            if board[location[0]][location[1]] == 0:
                positions = availablePlaces(location[0], location[1], board)
                if len(positions) > 0:
                    gameOver = 0

    if gameOver == 0:
        for j in range(15):
            for i in range(15):
                location = [j, i]
                if board[location[0]][location[1]] == 0:
                    positions = availablePlaces(location[0], location[1], board)
                    for p in positions:
                        for t in tileRack:
                            score = scoreMove(location, p, t, board, scoreBoard)
                            if scoreFunction(method, score, maxScore, scoreBoard, otherScoreBoard, turnNo, randomVars):
                                maxScore = score
                                bestLocation = [location, p, t]
        if len(bestLocation) != 0:
            for i in range(0, 6):
                if maxScore[1][i] == 18 and scoreBoard[i] != 18:
                    anotherGo = 1
            scoreBoard = setScoreBoard(maxScore[1], scoreBoard)
            board = placeTile(board, bestLocation)
            tileRack = removeTileFromRack(tileRack, bestLocation[2])
            tileRack, tileBag = refreshTileRack(tileRack, tileBag)
        else:
            # gameOver = 1
            print("Computer couldn't choose a move?")
            printGameState(board, tileRack, scoreBoard, 0)
            printGameState(board, tileRack, otherScoreBoard, 3)
            print(turnNo)
            print(maxScore)
            print(bestLocation)
            print(score)

    return board, scoreBoard, tileRack, tileBag, gameOver, anotherGo


def playTurnHuman(board, scoreBoard, otherScoreBoard, tileRack, tileBag, turnNo, numOfPlayers, method, randomVars):
    gameOver = 1

    for j in range(15):
        for i in range(15):
            location = [j, i]
            if board[location[0]][location[1]] == 0:
                positions = availablePlaces(location[0], location[1], board)
                if len(positions) > 0:
                    gameOver = 0

    if gameOver == 0:
        printTileRack(tileRack)
        tile = [0, 0]
        while tile not in tileRack:
            tile = input("Enter Tile Choice: ")
            tile = tile.split()
            tile[0] = int(tile[0])
            tile[1] = int(tile[1])

        error = 1
        position = [0, 0]
        while error == 1 or board[location[0]][location[1]] != 0 or board[position[0]][position[1]] != 0:
            error = 0
            location = input("Enter your value:")
            location = location.split(",")
            if len(location) == 2:
                position = location[1]
                location = location[0]
                location = location.split(" ")
                if len(location) == 2:
                    location[0] = int(location[0]) + 4 - numOfPlayers - 1
                    location[1] = int(location[1]) + 4 - numOfPlayers - 1
                else:
                    error = 1
                    print("input error")

                position = position.split(" ")
                if len(position) == 2:
                    position[0] = int(position[0]) + 4 - numOfPlayers - 1
                    position[1] = int(position[1]) + 4 - numOfPlayers - 1
                else:
                    error = 1
                    print("input error")
            else:
                error = 1
                print("input error")
            if error == 0:
                value = availablePlaces(location[0], location[1], board)
                if position not in value:
                    error = 1
                    print("not valid move")
                    #                print(board)
                    #                print(location)
                    #                print(position)
                    print(value)

        score = scoreMove(location, position, tile, board, scoreBoard)
        maxScore = score
        bestLocation = [location, position, tile]

        anotherGo = 0
        for i in range(0, 6):
            if maxScore[1][i] == 18 and scoreBoard[i] != 18:
                anotherGo = 1
        scoreBoard = setScoreBoard(maxScore[1], scoreBoard)
        board = placeTile(board, bestLocation)
        tileRack = removeTileFromRack(tileRack, bestLocation[2])
        tileRack, tileBag = refreshTileRack(tileRack, tileBag)

    return board, scoreBoard, tileRack, tileBag, gameOver, anotherGo
