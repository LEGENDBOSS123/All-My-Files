
INPUT = []
with open("paint.in") as file:
    INPUT = file.readlines()

def ANSWERFIND(INPUT):
    first = INPUT[0].split()
    first = [int(first[0]),int(first[1])]
    second = INPUT[1].split()
    second = [int(second[0]),int(second[1])]
    range1 = first[1]-first[0]
    range2 = second[1]-second[0]
    maximum_range = range1 + range2
    overlap = -min(0,max(first[1],second[1])-min(first[0],second[0]) - maximum_range)
    
    return maximum_range - overlap
    



file = open("paint.out","w")
file.write(str(ANSWERFIND(INPUT)))
