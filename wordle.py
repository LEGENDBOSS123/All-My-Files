
ANSWER = [list(input()),list(input()),list(input())]
GUESS = [list(input()),list(input()),list(input())]

def WORDLE(ANSWER,GUESS):
    RET = [0,0]
    GRID = [[0]*3,[0]*3,[0]*3]
    GRID2 = [[0]*3,[0]*3,[0]*3]
    for Y in range(3):
        for X in range(3):
            if ANSWER[Y][X] == GUESS[Y][X] and GRID[Y][X] == 0:
                GRID[Y][X] = 1
                RET[0] += 1
                
    for Y1 in range(3):
        for X1 in range(3):
            BREAK = False
            LETTER = GUESS[Y1][X1]
            if GRID[Y1][X1] == 0:
                for Y2 in range(3):
                    if BREAK:
                        break
                    for X2 in range(3):
                        if not BREAK and ANSWER[Y2][X2] == LETTER and GRID2[Y2][X2]==0 and GRID[Y2][X2]==0and [X1,Y1]!=[X2,Y2]:
                            RET[1] += 1
                            
                            GRID2[Y2][X2] = 1
                            BREAK = True
                            break
    
    return RET

RETURN = WORDLE(ANSWER,GUESS)
print(RETURN[0])
print(RETURN[1])
