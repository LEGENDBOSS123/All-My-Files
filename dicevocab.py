
INPUT1 = int(input())

DICE = [list(set(input())),list(set(input())),list(set(input())),list(set(input()))]
WORDS = []
for i in range(INPUT1):
    WORDS.append(list(input()))


for WORD in WORDS:
    USED = [1,1,1,1]
    LETTERS = [1]*len(WORD)
    DL = []
    for LETTER in range(len(WORD)):
        count = []
        for i in range(4):
            
            if USED[i] and WORD[LETTER] in DICE[i]:
                count.append(i)
        if len(count) == 0:
            break
            
        elif len(count) == 1:
            USED[count[0]] = 0
            LETTERS[LETTER] = 0
            
        elif len(count) > 1:
            DL.append([LETTER,count])
            
            
    for L in DL:
        for i in range(len(L[1])):
            c = L[1][i]
            if not USED[c]:
                L[1].remove(c)
        if len(L[1]) == 1:
            USED[c]=0
            LETTERS[L[0]]=0
        else:
            pass
                
                

        

        
    if list(set(LETTERS)) == [0]:
        print("YES")
    else:
        print("NO")
            
            
