


Qwerty = input("WHAT SHOULD I CALCULATE: ")



Bob = Qwerty.split(" ")
Tree = ["+","-","*","/","^"]

Lol = 0
Bagel = 0
Potato = 0
for Yeet in Bob:
    try:
        if int(Yeet) == int(Yeet):
            Bob[Lol] = int(Yeet)
            Potato+=1
    except:
        Bagel+=1
    Lol += 1


if Bagel+1==Potato:
    Goo = 0
    Lime = 1000000
    while len(Bob)!=1:
        Lol = 0
        for Yeet in Bob:
            try:
                if Yeet in Tree:
                    if int(Bob[Lol+1]) == int(Bob[Lol+1]):
                        if int(Bob[Lol+2]) == int(Bob[Lol+2]):
                            Dot = 0
                            if Yeet == Tree[0]:
                                Dot = Bob[Lol+1]+Bob[Lol+2]
                            elif Yeet == Tree[1]:
                                Dot = Bob[Lol+1]-Bob[Lol+2]
                            elif Yeet == Tree[2]:
                                Dot = Bob[Lol+1]*Bob[Lol+2]
                            elif Yeet == Tree[3]:
                                if Bob[Lol+2]!=0:
                                    Dot = Bob[Lol+1]/Bob[Lol+2]
                                else:
                                    Dot = 0
                            elif Yeet == Tree[4]:
                                Dot = Bob[Lol+1]**Bob[Lol+2]
                            Bob[Lol] = Dot
                            Bob.pop(Lol+2)
                            Bob.pop(Lol+1)
                            break
                                
                    
            except:
                pass
            
            Lol += 1
            Goo += 1
            
        if Goo>=Lime:
            print("THIS IS NOT A VALID PREFIX EXPRESSION")
            break
            
    if Goo >= Lime:
        pass
    else:
        YAY = Bob[0]
        print(YAY)
    
else:
    print("THIS IS NOT A VALID PREFIX EXPRESSION")
