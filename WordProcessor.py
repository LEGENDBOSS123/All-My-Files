

INPUT = []
with open("word.in") as file:
    INPUT = file.readlines()

def OUTPUT(INPUT):
    lines = 1
    current_limit = 0
    limit = int(INPUT[0].split()[1])

    for w in INPUT[1].split():
        l = len(w)
        if l+current_limit <= limit:
            current_limit += l
        elif l+current_limit > limit:
            current_limit = l
            lines+=1

    ret = [""]*lines
    current_limit = 0
    i = 0
    space = True
    for w in INPUT[1].split():
        l = len(w)
        if l+current_limit <= limit:
            current_limit += l
            if not space:
                ret[i] += " "+w
            else:
                space = False
                ret[i] += w
        elif l+current_limit > limit:
            i+=1
            current_limit = l
            ret[i] += w
    return ret
            


file = open("word.out","w")
out = OUTPUT(INPUT)
for i in range(len(out)):
    file.write(str(out[i]))
    file.write('\n')





