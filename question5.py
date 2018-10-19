#-*- coding: utf-8 -*-
from itertools import product

def getList():
    operation = ['+', '-', '']
    endResult=[]
    for each in product(operation, repeat=8):
        data = list('123456789')
        for i in range(8):
            data.insert(2*i + 1, each[i])
            calculate = ''.join(data)
        if eval(calculate) == 100:
            endResult.append(calculate)
    return endResult

if __name__ == '__main__':
    for i in getList():
        print('%s = 100' % i)

