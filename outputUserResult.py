def outputUserResult(totalNum, rightNum):
    print('结束！')
    if totalNum > rightNum:
        print('错了 ',totalNum-rightNum,' 题哦')
    else:
        print('全部正确，太棒了！')