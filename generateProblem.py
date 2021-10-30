from generateNum import generateNum
from generateSymbol import generateSymbol
import random
from computeAns import computeAns

num = random.randint(2, 4)


def generateProblem(level):
    if level == 1:
        list1 = generateNum(num, False, 100)
        list2 = generateSymbol(num, False)

    if level == 2:
        list1 = generateNum(num, False, 10000)
        list2 = generateSymbol(num, True)

    if level == 3:
        list1 = generateNum(num, True, 10000)
        list2 = generateSymbol(num, True)

    problem = fix(list1, list2)
    lens1 = len(list1)
    lens2 = len(list2)
    result1 = computeAns(list1[lens1 - 2:lens1], list2[lens2 - 1:])
    del list1[lens1 - 2]
    del list1[lens1 - 1]
    del list2[lens2 - 1]
    list1.append(result1)
    result = computeAns(list1, list2)

    return (problem, result)


def fix(list1, list2):
    lens = len(list1)
    ans = ""
    for i in range(lens):
        ans = ans + str(list1[i])
        if i < lens - 1:
            ans = ans + list2[i]
        if i == lens - 2:
            ans = ans + '('
        if i == lens:
            ans = ans + ')'

    return ans