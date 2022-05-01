
INPUT = []
with open("speeding.in") as file:
    INPUT = file.readlines()

def ANSWERFIND(INPUT):
    for i in range(len(INPUT)):
        INPUT[i] = INPUT[i].split()
        
    speedlimits = INPUT[1:int(INPUT[0][0])+1]
    speedlimits2 = INPUT[int(INPUT[0][0])+1:]
    counter = 0
    counter2 = 0
    
    



file = open("speeding.out","w")
file.write(str(ANSWERFIND(INPUT)))
