import random

LENGTH = int(input())
ORDER = input()

'''ORDER = "GHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHGHGH"
LENGTH = len(ORDER)

LENGTH = 2000
ORDER = "G" * LENGTH
ORDER = list(ORDER)

for i in range(LENGTH):
    if random.randint(0,1):
        ORDER[i] = "H"

    
ORDER = "".join(ORDER)

print(ORDER)'''

def LONELY(INPUT, LENGTH):
    COUNTER = 0
    GROUP = 3
    for X in range(LENGTH-2):
        for Y in range(LENGTH-GROUP+1):       
            if INPUT[Y:GROUP+Y].count("G") == 1 or INPUT[Y:GROUP+Y].count("H") == 1:
                COUNTER += 1
        GROUP += 1
                
    print(COUNTER)
    
def RLE_FIND(s):
    r = []
    current = s[0]
    num = 0
    for i in s+"ඞ":
        if i!=current:
            r.append([current,num])
            current = i
            num = 0
        
        num+=1
    return r
            
def LONELY2(INPUT, LENGTH):
    COUNTER = 0
    RLE = RLE_FIND(INPUT)
    RLE_LEN = len(RLE)
    for i in range(RLE_LEN):
        
        if i-1 >= 0 and RLE[i-1][1]>1:
            COUNTER += RLE[i-1][1]-1
        if i+1 < RLE_LEN and RLE[i+1][1]>1:
            COUNTER += RLE[i+1][1]-1
            
        if i-1 >= 0 and i+1<RLE_LEN and RLE[i][1]==1:
            COUNTER += RLE[i+1][1]*RLE[i-1][1]
            
            
    
    print(COUNTER)

#LONELY(ORDER,LENGTH)
LONELY2(ORDER,LENGTH)

