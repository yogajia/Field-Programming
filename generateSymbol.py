import random



def generateSymbol(n, Type):
    symbols = ['+', '-', '*', '/']
    result = []

    if (Type == True):
        for i in range(n - 1):
            a = random.randint(0, 3)
            result.append(symbols[a])
    elif (Type == False):
        for i in range(n - 1):
            a = random.randint(0, 1)
            result.append(symbols[a])
    return result
