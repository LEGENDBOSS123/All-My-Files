N = list(str(  1540670  ))
P = 3
D = 54
if int(N[-P])>=0 and int(N[-P])<=4:
    N[-P] = str(int(N[-P])+D)[-1]
    for i in range(P-1):
        N[-P+1+i] = "0"
else:
    N[-P] = str(abs(int(N[-P])-D))[0]
    for i in range(P-1):
        N[-P+1+i] = "0"

ANSWER = ""
for i in N:
    ANSWER+=i
ANSWER = int(ANSWER)
print(ANSWER)
