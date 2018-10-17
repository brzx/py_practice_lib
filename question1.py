#问题1 使用 for 循环、while 循环和递归写出 3 个函数来计算给定数列的总和。

def funfor(list):
    re = 0
    for i in list:
        re = re + i
    return re

def funwhile(list):
    re = 0
    i = 0
    le = len(list)
    while i < le:
        re = re + list[i]
        i = i + 1
    return re

def funrecursion(list):
    re = 0
    value = 0
    if len(list) == 1:
        re = list[0]
    else:
        value = list.pop()
        re = value + funrecursion(list)
    return re

if __name__ == '__main__':
    list = [5, 4, 3, 2, 1]
    print(funfor(list))
    print(funwhile(list))
    print(funrecursion(list))
    print(list)