import math

# This method returns the number of ways we can achieve sum_total
# given the numbers specified in the list_nums list.
# Every such numbers can be used as many number of times. 
def Combination(l, sum_total):
    
    
    comb = 0
    list_nums = l
    # Fill the body
    
    list_nums.sort(reverse = True)
    if sum_total == 0:
        return 1
    if sum_total == list_nums[-1]:
        return 1
    if sum_total < list_nums[-1]:
        return 0
    for e in list_nums:
        c = Combination(l,sum_total-e)
        print((e,c))
        comb+=c
    
    return comb
    

def test_combination():
    '''comb = Combination([1, 2], 4)
    if comb == 3:
        print(("Pass", comb))
    else:
        print(("Fail", comb))
    '''
    comb = Combination([1, 2, 4], 4)
    '''
    1,1,1,1
    
    '''
    if comb == 4:
        print(("Pass", comb))
    else:
        print(("Fail", comb))


test_combination()
