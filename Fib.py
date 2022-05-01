import math
STR_INPUT = input("TYPE A NUMBER: ")

REV_STR_INPUT = STR_INPUT[::-1]

index = 1

repeted = ""

for s in range(len(REV_STR_INPUT)//3):
    if REV_STR_INPUT[:index]*3 == REV_STR_INPUT[:index*3]:
        repeted = REV_STR_INPUT[:index*3]
    index+=1
    
non_repeted = STR_INPUT[:len(REV_STR_INPUT)-len(repeted)]
power = len(non_repeted)-2

OUTPUT_NUMERATOR = int(float(STR_INPUT)*10**(power+len(repeted)/3)) - int(float(STR_INPUT)*10**(power))
OUTPUT_DENOMINATOR = int(((10**(len(repeted)/3))-1)*10**(power))

GCD = math.gcd(OUTPUT_NUMERATOR,OUTPUT_DENOMINATOR)

print(str(OUTPUT_NUMERATOR//GCD)+'/'+str(OUTPUT_DENOMINATOR//GCD))
