from generateNum import generateNum
from generateSymbol import generateSymbol
import random
from computeAns import computeAns2

num = 2

def generateProblem(level):
    if level == 1:
        list1 = generateNum( num, False, 100)
        list2 = generateSymbol(num, False)
        problem = fix(list1,list2)
        result = computeAns2(list1,list2)

    if level == 2:
        list1 = generateNum( num, False, 10000)
        list2 = generateSymbol(num, True)
        problem = fix(list1,list2)
        result = computeAns2(list1,list2)

    if level == 3:
        list1 = generateNum( num, True, 10000)
        list2 = generateSymbol(num, True)
        problem = fix(list1,list2)
        result = computeAns2(list1,list2)

    return (problem, result)

def fix(list1, list2):
    lens = len(list1)
    ans = ""
    for i in range(lens):
        ans = ans + str(list1[i])
        if i < lens -1:
            ans = ans + list2[i]

    return ans
