
INPUT1 = int(input())
LIST = []
for i in range(INPUT1):
    a = input()
    b = list(map(int,input().split()))
    LIST.append(b)

def prime_factorize(d):
    prime_factors = []
    d1 = d
    index = 3
    if d!=0:
        while d1%2 == 0:
            d1 /= 2
            prime_factors.append(2)
        while index<d+1 and d1!=1:
            while d1%index == 0:
                d1 /= index
                prime_factors.append(index)
            index+=2
        if prime_factors == []:
            prime_factors.append(d1)
    return prime_factors

def find(l):
    s = sum(l)
    m = min(l)
    
    for i in range(len(l)):
        l[i]


    
for i in LIST:
    print(find(i))
