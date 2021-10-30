import random



def generateNum(n, Type, Num):
    result = []
    if (Type == True):
        for i in range(n):
            accuracy = random.randint(0, 2)
            a = random.uniform(0, Num)
            result.append(round(a, accuracy))
    elif (Type == False):
        for i in range(n):
            a = random.randint(0, Num)
            result.append(a)
    return result