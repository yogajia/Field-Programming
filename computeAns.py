import re
import functools


def formatInput(formula):
    """标准化输入表达式，去除多余空格等"""
    formula = formula.replace(' ', '')
    formula = formula.replace('++', '+')
    formula = formula.replace('+-', '-')
    formula = formula.replace('-+', '-')
    formula = formula.replace('--', '+')
    return formula


def mul_divOperation(s):
    """乘法除法运算"""
    s = formatInput(s)
    sub_str = re.search('(\d+\.?\d*[*/]-?\d+\.?\d*)', s)
    while sub_str:
        sub_str = sub_str.group()
        if sub_str.count('*'):
            l_num, r_num = sub_str.split('*')
            s = s.replace(sub_str, str(float(l_num) * float(r_num)))
        else:
            l_num, r_num = sub_str.split('/')
            s = s.replace(sub_str, str(float(l_num) / float(r_num)))

        s = formatInput(s)
        sub_str = re.search('(\d+\.?\d*[*/]\d+\.?\d*)', s)

    return s


def add_minusOperation(s):
    """加法减法运算
    思路：在最前面加上+号，然后正则匹配累加
    """
    s = formatInput(s)
    s = '+' + s
    tmp = re.findall('[+\-]\d+\.?\d*', s)
    s = str(functools.reduce(lambda x, y: float(x) + float(y), tmp))
    return s


def compute(formula):
    """无括号表达式解析"""
    # ret = formula[1:-1]
    ret = formatInput(formula)
    ret = mul_divOperation(ret)
    ret = add_minusOperation(ret)
    return ret


def computeAns(formula):
    """计算程序入口"""
    has_parenthesise = formula.count('(')
    formula = formatInput(formula)
    while has_parenthesise:
        sub_parenthesise = re.search('\([^()]*\)', formula)  # 匹配最内层括号
        if sub_parenthesise:
            formula = formula.replace(sub_parenthesise.group(), compute(sub_parenthesise.group()[1:-1]))
        else:
            has_parenthesise = False

    ret = compute(formula)
    return ret


if __name__ == '__main__':
    # print(mul_divOperation('17.0*7/3.0*3+1/2'))
    # print(add_minusOperation('1-2-3+1-4'))
    # print(calc('(9+8)*7/(5-2)*3+1/2'))
    s = "99+(1+2=(8)-(7+9))"

    print(calc("(1+2) - 3+4"))