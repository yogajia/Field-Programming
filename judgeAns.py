def judgeAns(userAns, ans):
    ans = round(ans, 2)
    user_str = str(userAns)
    if '.' in user_str:
        userAns = round(userAns, 2)
    if userAns == ans:
        return True
    else:
        return False
