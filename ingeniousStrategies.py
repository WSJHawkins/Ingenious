# -*- coding: utf-8 -*-
"""
@author: WSJHawkins
"""

#Decides what computer maximises
def scoreFunction(mode,score,maxScore,scoreBoard,otherScoreBoard,turnNo,randomVars):
    value = False

    #naive
    if(mode == 0):
        if(score[0] > maxScore[0]):
            value = True

    #considers min then total score if same
    elif(mode == 1):
        minScore = min(score[1])
        minScore2 = min(maxScore[1])
        if(minScore > minScore2):
            value = True
        elif(minScore == minScore2):
            if(score[0] > maxScore[0]):
                value = True

    #uses a weighting system based on raising the lowest pieces
    elif(mode == 2):
        copyOfScore = score[1].copy()
        copyOfScore.sort()
        copyOfMaxScore = maxScore[1].copy()
        copyOfMaxScore.sort()

        totalScore = 0
        multiplyer = 10
        for s in copyOfScore:
            totalScore = totalScore + multiplyer * s
            multiplyer = multiplyer - 1

        totalScore2 = 0
        multiplyer = 10
        for s in copyOfMaxScore:
            totalScore2 = totalScore2 + multiplyer * s
            multiplyer = multiplyer - 1

        if(totalScore > totalScore2):
            value = True

    #uses a comparisson system
    elif(mode == 3):
        copyOfScore = score[1].copy()
        copyOfScore.sort()
        copyOfMaxScore = maxScore[1].copy()
        copyOfMaxScore.sort()

        total = 0
        for i in range(0,6):
            total = total + ( (copyOfScore[i] - copyOfMaxScore[i]) * 1/(i+1) )


        if(total > 0):
            value = True

     #Pierre
    elif(mode == 4):
        copyOfScore = score[1].copy()
        copyOfScore.sort()
        copyOfMaxScore = maxScore[1].copy()
        copyOfMaxScore.sort()

        totalScore = 0
        for s in copyOfScore:
            if(s > 13):
                totalScore = totalScore + s/3
            elif(13 >= s > 11):
                totalScore = totalScore + s*0.8
            else:
                totalScore = totalScore + s

        maxScoreTotal = 0
        for s in copyOfMaxScore:
            if(s > 13):
                maxScoreTotal = maxScoreTotal + s/3
            elif(13>= s >11):
                maxScoreTotal = maxScoreTotal +s*0.8
            else:
                maxScoreTotal = maxScoreTotal + s

        if(totalScore > maxScoreTotal):
            value = True

    #Straight up maximisation
    elif(mode == 5):
        scoreCopy = score[1].copy()
        maxScoreCopy = maxScore[1].copy()

        if(scoreCopy > maxScoreCopy):
            value = True

    #same as 3 but compares to scoreboard
    elif(mode == 6):
        copyOfScore = score[1].copy()
        copyOfScore.sort()
        copyOfMaxScore = maxScore[1].copy()
        copyOfMaxScore.sort()

        total = 0
        for i in range(0,6):
            total = total + ( (copyOfScore[i] - scoreBoard[i]) * 1/(i+1) )

        maxScoreTotal = 0
        for i in range(0,6):
            maxScoreTotal = maxScoreTotal + ( (copyOfMaxScore[i] - scoreBoard[i]) * 1/(i+1) )
        if(total > maxScoreTotal):
            value = True


    #Takes turnNo into account, low turn number do 0 high turn number do 6
    elif(mode == 7):
        copyOfScore = score[1].copy()
        copyOfScore.sort()
        copyOfMaxScore = maxScore[1].copy()
        copyOfMaxScore.sort()

        total = 0
        for i in range(0,6):
            total = total + ( (copyOfScore[i] - scoreBoard[i]) * 1/(3*i+1) )
        total = score[0] * (1/(0.5*turnNo+1)) + total * (1-1/(0.5*turnNo+1))

        maxScoreTotal = 0
        for i in range(0,6):
            maxScoreTotal = maxScoreTotal + ( (copyOfMaxScore[i] - scoreBoard[i]) * 1/(2*i+1))
        maxScoreTotal = maxScore[0] * (1/(0.5*turnNo+1)) + maxScoreTotal * (1-1/(0.5*turnNo+1))

        if(total > maxScoreTotal):
            value = True

    #Piers2
    elif(mode==8):
        copyOfScore = score[1].copy()
        copyOfScore.sort()
        copyOfMaxScore = maxScore[1].copy()
        copyOfMaxScore.sort()
        difference=[0,0,0,0,0,0]
        difference1=[0,0,0,0,0,0]
        t1=0
        t2=0
        a = 0.4
        b = 0.01
        for i in range(0,6):
            difference[i] = copyOfScore[i] - scoreBoard[i]
            difference1[i] = copyOfMaxScore[i] - scoreBoard[i]

        totalScore = 0
        for i in range(0,6):
            if(copyOfScore[i]<=10):
                totalScore = totalScore + difference[i]
            elif(copyOfScore[i] <= 12):
                if(scoreBoard[i]<=10):
                    t1 = scoreBoard[i] + difference[i] - 10
                    t2 = 10 - scoreBoard[i]
                else:
                    t1 = 12 - scoreBoard[i]
                    t2 = 0
                totalScore = totalScore + t2 + t1*a
            else:
                if(scoreBoard[i]<10):
                    totalScore = (10-scoreBoard[i])+ 2*a + (copyOfScore[i] - 12)*b +totalScore
                elif(scoreBoard[i] < 13):
                    totalScore = (12 - scoreBoard[i])*a + (copyOfScore[i] - 12)*b + totalScore
                else:
                    totalScore = totalScore + difference[i]*b

        maxScoreTotal = 0
        for i in range(0,6):
             if(copyOfMaxScore[i]<=10):
                maxScoreTotal = maxScoreTotal + difference1[i]
             elif(copyOfMaxScore[i] <= 12):
                if(scoreBoard[i]<=10):
                    t1 = scoreBoard[i] + difference1[i] - 10
                    t2 = 10 - scoreBoard[i]
                else:
                    t1 = 12 - scoreBoard[i]
                    t2 = 0
                maxScoreTotal = maxScoreTotal + t2 + t1*a
             else:
                if(scoreBoard[i]<10):
                    maxScoreTotal = (10-scoreBoard[i])+ 2*a + (copyOfMaxScore[i] - 12)*b + maxScoreTotal
                elif(scoreBoard[i] < 13):
                    maxScoreTotal = (12 - scoreBoard[i])*a + (copyOfMaxScore[i] - 12)*b + maxScoreTotal
                else:
                    maxScoreTotal = maxScoreTotal + difference1[i]*b

        if(totalScore > maxScoreTotal):
            value = True


    #Makes decisions after looking at oponents points - optimised weights
    elif(mode == 9):
        alpha = randomVars[0]
        beta = randomVars[1]
        alpha2 = randomVars[2]
        beta2 = randomVars[3]
        alpha3 = randomVars[4]
        beta3 = randomVars[5]
        weight1 = (1/(alpha*turnNo+beta))
        weight2 = randomVars[6]
        weight3 = randomVars[7]


        copyOfScore = score[1].copy()
        copyOfMaxScore = maxScore[1].copy()
        copyOfScoreBoard = scoreBoard.copy()
        copyOfScoreBoard.sort()

        #sum up scores
        totalScore = score[0] * weight1
        totalScore2 = maxScore[0] * weight1

         #Always take the double go
        for i in range(0,6):
            if(score[1][i] == 18 and scoreBoard[i] != 18):
                totalScore = totalScore + 999
            if(maxScore[1][i] == 18 and scoreBoard[i] != 18):
                totalScore2 = totalScore2 + 999

        for i in range(0,6):
            val = copyOfScoreBoard.index(scoreBoard[i])
            totalScore = totalScore + weight2 * ( (copyOfScore[i] - scoreBoard[i]) * (1/(alpha2*val+beta2)) )
            totalScore = totalScore + weight3 * (copyOfScore[i]* (otherScoreBoard[i] - scoreBoard[i]) * (1/(alpha3*val+beta3)))
            totalScore2 = totalScore2 + weight2 * ( (copyOfMaxScore[i] - scoreBoard[i]) * (1/(alpha2*val+beta2)) )
            totalScore2 = totalScore2 + weight3 * (copyOfMaxScore[i]* (otherScoreBoard[i] - scoreBoard[i]) * (1/(alpha3*val+beta3)) )

        if(totalScore > totalScore2):
            value = True

        #Means it always picks something
        if(maxScore[0] == 0):
            value = True

    return value