from generateNum import generateNum
from generateSymbol import generateSymbol
import random
from computeAns import computeAns


def generateProblem(level):
    num = random.randint(2, 4)
    if level == 1:
        list1 = generateNum(num, False, 100)
        list2 = generateSymbol(num, False)
        problem = fix(list1, list2)
        result = float(computeAns(problem))

    if level == 2:
        list1 = generateNum(num, False, 10000)
        list2 = generateSymbol(num, True)
        problem = fix(list1, list2)
        result = float(computeAns(problem))

    if level == 3:
        list1 = generateNum(num, True, 10000)
        list2 = generateSymbol(num, True)
        problem = fix(list1, list2)
        result = float(computeAns(problem))

    return (problem, result)


def fix(num, symbol):
    numLen = len(num)
    if numLen < 4:
        ans = ""
        for i in range(numLen):
            ans = ans + str(num[i])
            if i < numLen - 1:
                ans = ans + symbol[i]
        return ans
    else:
        pos = random.randint(0, 2)
        ans = ""
        for i in range(numLen):
            if i == pos:
                ans += "("
            ans += str(num[i])
            if i == pos + 1:
                ans += ")"
            if i < numLen - 1:
                ans = ans + symbol[i]
        return ans
