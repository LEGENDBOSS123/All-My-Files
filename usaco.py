
INPUT = []
with open("hps.in") as file:
    INPUT = file.readlines()

def ANSWERFIND(INPUT):
    all_inputs = INPUT[1:]
    for i in range(len(all_inputs)):
        e = all_inputs[i].split()
        all_inputs[i]=[int(e[0]),int(e[1])]
    combos = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    ret = 0
    for z in combos:
        ret2 = 0
        for i in all_inputs:
            if [z[0],z[1]] == i:
                ret2+=1
            elif [z[1],z[2]] == i:
                ret2+=1
            elif [z[2],z[0]] == i:
                ret2+=1
            
        if ret2>ret:
            ret = ret2
    return ret
        
    
    



file = open("hps.out","w")
file.write(str(ANSWERFIND(INPUT)))
