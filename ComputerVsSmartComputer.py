# the smart computer is gonna make the first move
import random
def checkWinner(xState, oState, Xwin, Xlose):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]]
    # print(xState)
    # print(oState)
    for win in wins:
        if xState[win[0]] + xState[win[1]] + xState[win[2]] == 3:
            # print("X won the game!!")
            Xwin[0] += 1
            return 1
        if oState[win[0]] + oState[win[1]] + oState[win[2]] == 3:
            # print("O won the game!!")
            Xlose[0] += 1
            return 1
    return 0
if __name__ == "__main__":
    draw = 0
    Xwin = [0]
    # why [0] and not simply 0?
    # ans: its relevance is attached ot line 10 i.e you can't change an integer by passing it to a function in python as integers are immutable but list can be changed like we have done.
    Xlose = [0]
    t = 100000
    while(t):
        xState = [0,0,0,0,0,0,0,0,0] 
        oState = [0,0,0,0,0,0,0,0,0]
        Choices_left = [0,1,2,3,4,5,6,7,8]
        chance = 1
        turns = 9
        opponentList = []
        t -= 1
        while(turns):
            # printBoard(xState, oState)
            if chance:
                if opponentList == []:
                    val = 0
                else:
                    if opponentList[0] == 1:
                        val = 6
                        if len(opponentList) >= 2 and opponentList[1] == 3:
                            val = 8
                            if len(opponentList) == 3 and opponentList[2] == 4:
                                val = 7
                            elif len(opponentList) == 3 and opponentList[2] == 7:
                                val = 4 
                            elif len(opponentList) == 3:
                                val = 4
                        elif len(opponentList) >= 2 :
                            val = 3

                    elif opponentList[0] == 3:
                        val = 2
                        if len(opponentList) >= 2 and opponentList[1] == 1:
                            val = 8
                            if len(opponentList) == 3 and opponentList[2] == 4:
                                val = 5
                            elif len(opponentList) == 3 and opponentList[2] == 5:
                                val = 4
                            elif len(opponentList) == 3:
                                val = 4
                        elif len(opponentList)>=2 :
                            val = 1

                    elif opponentList[0] == 2:
                        val = 6
                        if len(opponentList) >= 2 and opponentList[1] == 3:
                            val = 8
                            if len(opponentList) == 3 and opponentList[2] == 7:
                                val = 4
                            elif len(opponentList) == 3 and opponentList[2] == 4:
                                val = 7
                            elif len(opponentList) == 3:
                                val = 4
                        elif len(opponentList)>=2 :
                            val = 3

                    elif opponentList[0] == 6:
                        val = 2
                        if len(opponentList) >=2 and opponentList[1] == 1:
                            val = 8
                            if len(opponentList) == 3 and opponentList[2] == 4:
                                val = 5
                            elif len(opponentList) == 3 and opponentList[2] == 5:
                                val = 4
                            elif len(opponentList) == 3:
                                val = 4
                        elif len(opponentList)>=2 :
                            val = 1

                    elif opponentList[0] == 5:
                        val = 2
                        if len(opponentList) >= 2 and opponentList[1] == 1:
                            val = 6
                            if len(opponentList) == 3 and opponentList[2] == 3:
                                val = 4
                            elif len(opponentList) == 3 and opponentList[2] == 4:
                                val = 3
                            elif len(opponentList) == 3:
                                val = 4
                        elif len(opponentList)>=2 :
                            val = 1

                    elif opponentList[0] == 7:
                        val = 6
                        if len(opponentList) >=2 and opponentList[1] == 3:
                            val = 2
                            if len(opponentList) == 3 and opponentList[2] == 1:
                                val = 4
                            elif len(opponentList) == 3 and opponentList[2] == 4:
                                val = 1
                            elif len(opponentList) == 3:
                                val = 4
                        elif len(opponentList)>=2 :
                            val = 3

                    elif opponentList[0] == 8:
                        val = 2
                        if len(opponentList) >=2 and opponentList[1] == 1:
                            val = 6
                            if len(opponentList) == 3 and opponentList[2] == 4:
                                val = 3
                            elif len(opponentList) == 3 and opponentList[2] == 3:
                                val = 4
                            elif len(opponentList) == 3:
                                val = 4
                        elif len(opponentList)>=2 :
                            val = 1
                    else:
                        val = 8
                        if len(opponentList)>=2 and opponentList[1] == 1:
                            val = 7
                            if len(opponentList)>=3 and opponentList[2] == 6:
                                val = 2
                                if len(opponentList)>=4 and opponentList[3] == 5:
                                    val = 3
                                elif len(opponentList)>=4:
                                    val = 5
                            elif len(opponentList)>=3 :
                                val = 6

                        if len(opponentList)>=2 and opponentList[1] == 3:
                            val = 5
                            if len(opponentList)>=3 and opponentList[2] == 2:
                                val = 6
                                if len(opponentList)>=4 and opponentList[3] == 7:
                                    val = 1
                                elif len(opponentList)>=4:
                                    val = 7
                            elif len(opponentList)>=3 :
                                val = 2
                        if len(opponentList)>=2 and opponentList[1] == 5:
                            val = 3
                            if len(opponentList)>=3 and opponentList[2] == 6:
                                val = 2
                                if len(opponentList)>=4 and opponentList[3] == 1:
                                    val = 7
                                elif len(opponentList)>=4:
                                    val = 1
                            elif len(opponentList)>=3 :
                                val = 6
                        if len(opponentList)>=2 and opponentList[1] == 7:
                            val = 1
                            if len(opponentList)>=3 and opponentList[2] ==2 :
                                val = 6
                                if len(opponentList)>=4 and opponentList[3] == 3:
                                    val = 5
                                elif len(opponentList)>=4:
                                    val = 3
                            elif len(opponentList)>=3 :
                                val = 2
                        if len(opponentList)>=2 and opponentList[1] == 2:
                            val = 6
                            if len(opponentList)>=3 and opponentList[2] == 3:
                                val = 7
                            elif len(opponentList)>=3 and opponentList[2] == 7:
                                val = 3
                            elif len(opponentList)>=3 :
                                val = 3
                        if len(opponentList)>=2 and opponentList[1] == 6:
                            val = 2
                            if len(opponentList)>=3 and opponentList[2] == 1:
                                val = 5
                            elif len(opponentList)>=3 and opponentList[2] == 5:
                                val = 1
                            elif len(opponentList)>=3 :
                                val = 1
                xState[val] = 1  
                # printBoard(xState, oState)     
            else:
                while(True):
                    val = random.choice(range(9))
                    if xState[val] == 0 and oState[val] == 0: 
                        break 
                oState[val] = 1
                opponentList.append(val)
                    
            
            if checkWinner(xState, oState, Xwin, Xlose):
                break
            chance = 1 - chance
            turns -= 1
            if(turns == 0):
                draw += 1
    print(f"X won in {Xwin[0]} cases, O won in {Xlose[0]} cases and {draw} games resulted in a draw")

