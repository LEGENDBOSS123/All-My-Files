
INPUT = []
with open("billboard.in") as file:
    INPUT = file.readlines()
def AREA(I):
    return abs(I[0]-I[2]) * abs(I[1]-I[3])


def POINT_IN(POINT,BOX):
    if abs(POINT[0]-BOX[0]) + abs(POINT[0]-BOX[2]) == abs(BOX[0]-BOX[2]):
        if abs(POINT[1]-BOX[1]) + abs(POINT[1]-BOX[3]) == abs(BOX[1]-BOX[3]):
            return True
    return False

    
def AREA_CALCULATE(I):
    BILLBOARD1 = list(map(int,I[0].split()))
    BILLBOARD2 = list(map(int,I[1].split()))
    TRUCK = list(map(int,I[2].split()))
    TOTAL_AREA = AREA(BILLBOARD1) + AREA(BILLBOARD2)
    X_DIS = (BILLBOARD1[2]-BILLBOARD1[0]+TRUCK[2]-TRUCK[0]-max(BILLBOARD1[0],BILLBOARD1[2],TRUCK[0],TRUCK[2])+min(BILLBOARD1[0],BILLBOARD1[2],TRUCK[0],TRUCK[2]))
    Y_DIS = (BILLBOARD1[3]-BILLBOARD1[1]+TRUCK[3]-TRUCK[1]-max(BILLBOARD1[1],BILLBOARD1[3],TRUCK[1],TRUCK[3])+min(BILLBOARD1[1],BILLBOARD1[3],TRUCK[1],TRUCK[3]))
    INTERSECTION_AREA1 = X_DIS * Y_DIS
    if X_DIS < 0 or Y_DIS < 0:
        INTERSECTION_AREA1 = 0
    X_DIS = (BILLBOARD2[2]-BILLBOARD2[0]+TRUCK[2]-TRUCK[0]-max(BILLBOARD2[0],BILLBOARD2[2],TRUCK[0],TRUCK[2])+min(BILLBOARD2[0],BILLBOARD2[2],TRUCK[0],TRUCK[2]))
    Y_DIS = (BILLBOARD2[3]-BILLBOARD2[1]+TRUCK[3]-TRUCK[1]-max(BILLBOARD2[1],BILLBOARD2[3],TRUCK[1],TRUCK[3])+min(BILLBOARD2[1],BILLBOARD2[3],TRUCK[1],TRUCK[3]))
    INTERSECTION_AREA2 = X_DIS * Y_DIS
    if X_DIS < 0 or Y_DIS < 0:
        INTERSECTION_AREA2 = 0
    return TOTAL_AREA - INTERSECTION_AREA1 - INTERSECTION_AREA2
    
    


file = open("billboard.out","w")
file.write(str(AREA_CALCULATE(INPUT)))
