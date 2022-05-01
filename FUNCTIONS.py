import random
import time


current_milli_time = lambda: int(round(time.time() * 1000))

Min_Max = 500000
Min = random.randint(0, Min_Max // 2)
Max = random.randint(Min_Max, 2*Min_Max)

papas_list = []
how_many_numbers_in_the_list = 100

for i in range(how_many_numbers_in_the_list):
    papas_list.append(random.randint(Min, Max))
#print(papas_list)

#the coding actually starts here

def sort_list(LIST):
    #find a number less than the min number in the list
    MIN = 0
    for i in LIST:
        if i < MIN:
            MIN = i
           
    new_list = []
    count = MIN-1
    
    while True:
        for i in LIST:
            if i == count:
                new_list.append(i)
        if len(new_list) == len(LIST):
            break
        count+=1

    return new_list

ts_ms_orig = current_milli_time()
new_list = sort_list(papas_list)
ts_ms_final = current_milli_time()

print(new_list)
print("Time is msec for my function: ", ts_ms_final - ts_ms_orig)

ts_ms_orig = current_milli_time()
papas_list.sort()
ts_ms_final = current_milli_time()
print(papas_list)

print("Time is msec for python sort function: ", ts_ms_final - ts_ms_orig)

#print(sort_list(papas_list))
