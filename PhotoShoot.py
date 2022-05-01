INPUT = int(input())
G = []
L = []
for i in range(INPUT):
    i = input().split()
    if i[0]=="G":
        G.append(int(i[1]))
    if i[0]=="L":
        L.append(int(i[1]))
OUTPUT = 0
G.sort(reverse = True)
L.sort()
while len(G)>0 and len(L)>0 and G[0]>L[0]:
    
    t = 0
    i = 0
    while i<len(G):
        if G[i]>L[0]:
            t+=1
        else:
            break
        i+=1
        
        
    t1 = 0
    i1 = 0
    while i1<len(L):
        if G[0]>L[i1]:
            t1+=1
        else:
            break
        i1+=1
        
    if t<t1:
        G.pop(0)
    elif t>t1:
        L.pop(0)
    else:
        G.pop(0)
        
    OUTPUT+=1




    






print(OUTPUT)