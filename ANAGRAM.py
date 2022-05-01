#QUESTION 1 ANSWER
#"""

#"""


#QUESTION 2 ANSWER
"""

string1 = string1 = input().replace(" ","").lower()

def FIND_ISOMORPHIC(string1):
    s1 = list(set(str(string1)))
    s2 = list(str(string1))
    s1.sort()
    s2.sort()
    if s1==s2:
        return True
    else:
        return False


print(FIND_ISOMORPHIC(string1))
"""

    
# QUESTION 3 ANSWER
"""
string1 = input().replace(" ","").lower()
string2 = input().replace(" ","").lower()
def FIND_ANAGRAM(string1,string2):
    s1 = list(string1)
    s2 = list(string2)
    num = 0
    for i in s1:
        for a in s2:
            if i==a:
                num+=1
                break
            
    if num == len(s1) and num == len(s2):
        return True
    else:
        return False

print(FIND_ANAGRAM(string1,string2))
"""


#QUESTION 4 ANSWER
#"""

#"""

#QUESTION 5 ANSWER
#"""

#"""

#QUESTION 1 ANSWER
#"""

#"""

#QUESTION 1 ANSWER
#"""

#"""


