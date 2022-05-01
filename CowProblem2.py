LENGTH = int(input())
#LENGTH = 6
NUMBERS = list(map(int,input().split()))
#NUMBERS = [1,5,3,3,4,1]
GOAL = list(map(int,input().split()))
#GOAL = [1,2,2,2,1,3]
MOVES = 0
DISPLACEMENT = [GOAL[i] - NUMBERS[i] for i in range(LENGTH)]
def COMPUTE(D,L):
    D2 = L*[0]
    
    start = -1
    a = 0
    Min = 0
    for i in range(L):
        if a!= -1:
            if D[i] > 0:
                if start == -1:
                    start = i
                    D2[i] = -1
                    a = 1
                else:
                    D2[i] = -1
                
            elif D[i] <= 0 and start != -1:
                break
        if a!= 1:
            if D[i] < 0 and a != 1:
                if start == -1:
                    start = i
                    D2[i] = 1
                    a = -1
                else:
                    D2[i] = 1
                
            elif D[i] >= 0 and start != -1:
                break   
    return D2
        
while(DISPLACEMENT.count(0) != LENGTH):
    #print(DISPLACEMENT)
    DISPLACEMENT = [x+y for x,y in zip(DISPLACEMENT,COMPUTE(DISPLACEMENT,LENGTH))]
    
    MOVES+=1

print(MOVES)

    
