
INPUT = []
with open("buckets.in") as file:
    INPUT = file.readlines()

def PATHFIND(INPUT):
    B = []
    L = []
    R = []
    for y in range(len(INPUT)):
        for x in range(len(INPUT[y])):
            if INPUT[y][x] == "B":
                B = [x,y]
            elif INPUT[y][x] == "L":
                L = [x,y]
            elif INPUT[y][x] == "R":
                R = [x,y]

    
    if R[0] > min(B[0],L[0]) and R[0] < max(B[0],L[0]) and R[1] > min(B[1],L[1]) and R[1] < max(B[1],L[1]):
        if abs(B[0]-L[0]) == 0 or abs(B[1]-L[1]) == 0:
            return abs(B[0]-L[0]) + abs(B[1]-L[1]) + 1
        else:
            return abs(B[0]-L[0]) + abs(B[1]-L[1]) - 1
    return abs(B[0]-L[0]) + abs(B[1]-L[1]) - 1
            


file = open("buckets.out","w")
file.write(str(PATHFIND(INPUT)))
