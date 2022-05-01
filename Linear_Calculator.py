

INPUT = list(map(int,input().split()))
LEN_MATRIX = len(INPUT)
MATRIX = LEN_MATRIX*[0]

MATRIX[0] = INPUT

for i in range(LEN_MATRIX-1):
    MATRIX[i+1] = list(map(int,input().split()))


print(MATRIX)
