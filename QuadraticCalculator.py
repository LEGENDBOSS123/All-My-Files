import math
a = eval(input("a = "))
b = eval(input("b = "))
c = eval(input("c = "))
prime_factors = []
inside = 1
outside = 1
d = b**2-4*a*c
i = ""

if d<0:
    i = "i"
    d *= -1
sqrtd = (math.sqrt(d))
nosqrt = False
if int(sqrtd)==sqrtd:
    nosqrt = True
    outside = sqrtd
else:  
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
    
    for prime in set(prime_factors):
        c = prime_factors.count(prime)
        if c%2 == 1:
            inside *= prime
            outside *= prime**((c-1)/2)
        else:
            outside *= prime**(c/2)
        
solution1 = 0
solution2 = 0
gcd = math.gcd(math.gcd(int(outside),-b),2*a)

a = a/gcd
outside = outside/gcd
b = b/gcd

if nosqrt:
    if i == "i":
        if outside == 0:
            solution1 = str(int(-b))+"/"+str(int(2*a))
            solution2 = str(int(-b))+"/"+str(int(2*a))
        else:
            solution1 = "("+str(int(-b))+" + "+str(int(outside))+i+")"+"/"+str(int(2*a))
            solution2 = "("+str(int(-b))+" - "+str(int(outside))+i+")"+"/"+str(int(2*a))
        
    else:
        
        solution1 = str(-b+outside)+"/"+str(2*a)
        solution2 = str(-b-outside)+"/"+str(2*a)
else:
    if outside == 1:
        solution1 = "("+str(int(-b))+" + "+i+"√"+str(int(inside))+")"+"/"+str(int(2*a))
        solution2 = "("+str(int(-b))+" - "+i+"√"+str(int(inside))+")"+"/"+str(int(2*a))
    else:
        solution1 = "("+str(int(-b))+" + "+str(int(outside))+i+"√"+str(int(inside))+")"+"/"+str(int(2*a))
        solution2 = "("+str(int(-b))+" - "+str(int(outside))+i+"√"+str(int(inside))+")"+"/"+str(int(2*a))

print(solution1)
print(solution2)
