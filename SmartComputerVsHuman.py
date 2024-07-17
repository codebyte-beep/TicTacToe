# note: in this code the smart computer is gonna make the first move
def printBoard(xState, oState):
    zero = "X" if xState[0] else ("O" if oState[0] else " ")
    one = "X" if xState[1] else ("O" if oState[1] else " ")
    two = "X" if xState[2] else ("O" if oState[2] else " ")
    three = "X" if xState[3] else ("O" if oState[3] else " ")
    four = "X" if xState[4] else ("O" if oState[4] else " ")
    five = "X" if xState[5] else ("O" if oState[5] else " ")
    six = "X" if xState[6] else ("O" if oState[6] else " ")
    seven = "X" if xState[7] else ("O" if oState[7] else " ")
    eight = "X" if xState[8] else ("O" if oState[8] else "  ")
    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")

def checkWinner(xState, oState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]]
    # print(xState)
    # print(oState)
    for win in wins:
        if xState[win[0]] + xState[win[1]] + xState[win[2]] == 3:
            print("X won the game!!")
            return 1
        if oState[win[0]] + oState[win[1]] + oState[win[2]] == 3:
            print("O won the game!!")
            return 1
    return 0

if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0] 
    oState = [0,0,0,0,0,0,0,0,0]
    Choices_left = [0,1,2,3,4,5,6,7,8]
    chance = 1
    turns = 9
    opponentList = []
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
            printBoard(xState, oState)     
        else:
            while(True):
                try:
                    while(True):
                        val = int(input("O's chance: "))
                        if xState[val] == 0 and oState[val] == 0:
                            break
                        else:
                            print("Please choose a valid option")
                    oState[val] = 1
                    opponentList.append(val)
                    break
                except Exception as e:
                    print("Please choose a valid option")
        
        if checkWinner(xState, oState):
            break
        chance = 1 - chance
        turns -= 1
        if(turns == 0):
            print("The match was a draw!!")