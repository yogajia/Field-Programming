def getUserInput():
    level = 1
    print("输出：请输入你的年级")
    grade = input("输入：")
    if grade in ["一年级", "二年级"]:
        level = 1
    if grade in ["三年级", "四年级"]:
        level = 2
    if grade in ["五年级", "六年级"]:
        level = 3
    print("输出：请输入题目数")
    num = input("输入：")
    return level, int(num)

# print(getUserInput())
