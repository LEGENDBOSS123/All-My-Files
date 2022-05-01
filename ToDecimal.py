def BASE_TO_DECIMAL():
    BASE_INPUT = input("BASE: ")
    if BASE_INPUT.isdigit():
        if int(BASE_INPUT)>16:
            return False
        else:
            BASE_INPUT = int(BASE_INPUT)
    else:
        return False
    NUMBER_INPUT = input("NUMBER: ")
    RETURN_NUMBER = 0
    REV_NUMBER_INPUT = NUMBER_INPUT[::-1]
    SKIPPED = 0
    for INDEX in range(len(REV_NUMBER_INPUT)):
        NUMBER_AT_INDEX = REV_NUMBER_INPUT[INDEX]
        if NUMBER_AT_INDEX.isdigit():
            NUMBER_AT_INDEX=int(REV_NUMBER_INPUT[INDEX])
        elif NUMBER_AT_INDEX == "_":
            SKIPPED += 1
            continue
        elif NUMBER_AT_INDEX.upper() == "A":
            NUMBER_AT_INDEX = 10
        elif NUMBER_AT_INDEX.upper() == "B":
            NUMBER_AT_INDEX = 11
        elif NUMBER_AT_INDEX.upper() == "C":
            NUMBER_AT_INDEX = 12
        elif NUMBER_AT_INDEX.upper() == "D":
            NUMBER_AT_INDEX = 13
        elif NUMBER_AT_INDEX.upper() == "E":
            NUMBER_AT_INDEX = 14
        elif NUMBER_AT_INDEX.upper() == "F":
            NUMBER_AT_INDEX = 15
        else:
            return False
        if NUMBER_AT_INDEX+1>BASE_INPUT:
            return False
        RETURN_NUMBER+=NUMBER_AT_INDEX*BASE_INPUT**(INDEX-SKIPPED)
    print("the inbuilt function outputs: "+str(int(NUMBER_INPUT,BASE_INPUT)))
    return RETURN_NUMBER
while True:
    var = str(BASE_TO_DECIMAL())
    print("my function outputs: "+var)
