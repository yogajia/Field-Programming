# input:
# num: a list of Integer or Decimal
# symbol: a list of (+, - , *, /)

# output:
# ans: the result of the calculation

def computeAns(num, symbol):
    for i in range(len(num)):
        if len(symbol)!=0:
        if symbol[i] == '*' or symbol[i] == '/':
            if symbol[i] == '*':
                ans = num[i] * num[i + 1]
            elif symbol[i] == '/':
                ans = num[i] / num[i + 1]
            num.insert(i, ans)
            num.pop(i + 1)
            num.pop(i + 1)
            symbol.pop(i)
            print(i)
            print(num)
            print(symbol)

    ans = num[0]
    for i in range(len(symbol)):
        if symbol[i] == '+':
            ans += num[i + 1]
        elif symbol[i] == '-':
            ans -= num[i + 1]

    return ans


def computeAns2(num, symbol):
    if symbol[0] == '+':
        ans = num[0] + num[1]
    elif symbol[0] == '-':
        ans = num[0] - num[1]
    elif symbol[0] == '*':
        ans = num[0] * num[1]
    else:
        ans = num[0] / num[1]
    return ans
# num1 = [100, 200, 300, 400]
# num2 = [2.2, 200, 123, 300]
# num3 = [5, 2, 3, 1]
#
# symbol1 = ['+', '-', '*']
# symbol2 = ['-', '-', '-']
# symbol3 = ['/', '/', '/']
#
# ans1 = num1[0] + num1[1] - num1[2] * num1[3]
# temp_ans1 = computeAns(num1, symbol1)
# print(temp_ans1, ans1)
# print(temp_ans1 == ans1)
#
# ans2 = num2[0] - num2[1] - num2[2] - num2[3]
# temp_ans2 = computeAns(num2, symbol2)
# print(temp_ans2, ans2)
# print(temp_ans2 == ans2)
#
# ans3 = num3[0] / num3[1] / num3[2] / num3[3]
# temp_ans3 = computeAns(num3, symbol3)
# print(temp_ans3, ans3)
# print(temp_ans3 == ans3)


