def printBoard(xState, oState):
    zero = "X" if xState[0] else ("O" if oState[0] else 0)
    one = "X" if xState[1] else ("O" if oState[1] else 1)
    two = "X" if xState[2] else ("O" if oState[2] else 2)
    three = "X" if xState[3] else ("O" if oState[3] else 3)
    four = "X" if xState[4] else ("O" if oState[4] else 4)
    five = "X" if xState[5] else ("O" if oState[5] else 5)
    six = "X" if xState[6] else ("O" if oState[6] else 6)
    seven = "X" if xState[7] else ("O" if oState[7] else 7)
    eight = "X" if xState[8] else ("O" if oState[8] else 8)
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
    chance = 1
    turns = 9
    val = 0
    while(turns):
        # printBoard(xState, oState)
        print(val)
        if chance:
            val = int(input("X's chance: "))
            xState[val] = 1
        else:
            val = int(input("O's chance: "))
            oState[val] = 1
        printBoard(xState, oState)
        if checkWinner(xState, oState):
            break
        chance = 1 - chance
        turns -= 1





    
