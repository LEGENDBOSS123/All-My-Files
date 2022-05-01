import math

INPUT = open("gymnastics.in").readlines()[1:]

for i in range(len(INPUT)):
    INPUT[i] = INPUT[i].split()

def FIND_ANSWER(I):
    RETURN = 0
    LENGTH = len(I[0])
    CASES = len(I)
    LIST = [set([-1])]*LENGTH
    print(LIST)
    for x in range(CASES):
        for y in range(LENGTH):
            
            if -1 in LIST[int(I[x][y])-1]:
                LIST[int(I[x][y])-1] = set(I[x][y+1:])
            else:
                
                LIST[int(I[x][y])-1] = LIST[int(I[x][y])-1].intersection(set(I[x][y+1:]))
                
    for x in range(LENGTH):
        l = len(LIST[x])
        RETURN += int(l)
        
    
    return RETURN

OUTPUT = FIND_ANSWER(INPUT)
#print(OUTPUT)
open("gymnastics.out","w").write(str(OUTPUT))
