import random
def printBoard(xState, oState):
    # python's variation of ternary operator
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

# def minimax():
if __name__ == "__main__":
    # as the name sounds xState and oState shows their respective states an any point in time. whichever index
    # the user chooses becomes 1 otherwise remains 0
    xState = [0,0,0,0,0,0,0,0,0] 
    oState = [0,0,0,0,0,0,0,0,0]
    # for storing the options computer is left to choose with
    compChoice = [0,1,2,3,4,5,6,7,8]
    chance = 1
    turns = 9
    printBoard(xState, oState)
    while(turns):
        # printBoard(xState, oState)
        if chance:
            while(True):
                # this try and except block will avoid errors such as choosing already chosen option and an invalid input such as string
                try:
                    val = int(input("X's chance: "))
                    # 51st line has to be written over 52nd line to avoid error in which the already chosen option is chosen again
                    compChoice.remove(val)
                    xState[val] = 1
                    break
                except Exception as e:
                    print("Please choose a valid option")
        else:
            val = random.choice(compChoice)
            print(f"O/computer's chance: {val}")
            oState[val] = 1
            compChoice.remove(val)
            printBoard(xState, oState)
        if checkWinner(xState, oState):
            printBoard(xState, oState)
            break
        # for alternate chances 
        chance = 1 - chance
        turns -= 1





    
