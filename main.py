from judgeAns import judgeAns
from getUserInput import getUserInput
from generateProblem import generateProblem
from outputUserResult import outputUserResult


if __name__ == '__main__':
    total, right = 0, 0
    level, num = getUserInput()
    for i in range(num):
        total += 1
        problem, ans = generateProblem(level)
        print(problem, ans)
        print("输出：", problem)
        userAns = float(input("输入："))
        if judgeAns(userAns, ans):
            # print("yes!!!!!!!!!!!!!!!!!!!!!!!")
            right += 1

    outputUserResult(total, right)
