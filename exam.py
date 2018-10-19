import pdb


def dg(l):
    if len(l) > 1:
        y = l.pop() + dg(l)
    else:
        y = l.pop()
    return y

def jchb(l1, l2):
    res_list = []
    if len(l1) == len(l2):
        i = 0
        while i < len(l1):
            res_list.append(l1[i])
            res_list.append(l2[i])
            i = i + 1
    elif len(l1) < len(l2):
        i = 0
        while i < len(l2):
            if i < len(l1):
                res_list.append(l1[i])
                res_list.append(l2[i])
            else:
                res_list.append(l2[i])
            i = i + 1
    else:
        i = 0
        while i < len(l1):
            if i < len(l2):
                res_list.append(l1[i])
                res_list.append(l2[i])
            else:
                res_list.append(l1[i])
            i = i + 1
    return res_list

def fbnq(li):
    res_li = []
    res_li.append(li[0])
    res_li.append(li[1])
    rg = range(100)
    for i in rg:
        if i < 2:
            pass
        else:
            res_li.append(res_li[i-1]+res_li[i-2])
    return res_li

def plzd1(li):
    res_li = map(lambda x: str(x), li)
    res_li.sort()
    res_li.reverse()
    return int(reduce(lambda x,y: x+y, res_li))

def plzd2(li, x):
    res_li = []


if __name__ == '__main__':
    print 'question 1-----------------------------------------------------------------'
    li = range(5)
    print li
    z = dg(li)
    print z
    print 'question 2-----------------------------------------------------------------'
    li1 = ['a', 'B', 'C']
    li2 = [1, 2, 3]
    print li1
    print li2
    print jchb(li1, li2)
    li3 = ['a', 'B', 'C']
    li4 = [1, 2, 3, 4, 5]
    #pdb.set_trace()
    print li3
    print li4
    print jchb(li3, li4)
    li5 = ['a', 'b', 'C', 'D', 'e']
    li6 = [4, 7, 9]
    print li5
    print li6
    print jchb(li5, li6)
    print 'question 3-----------------------------------------------------------------'
    print fbnq([0, 1])
    print 'question 4-----------------------------------------------------------------'
    li7 = [50, 2, 1, 9]
    li8 = [93, 24, 95, 46, 8]
    li9 = [73, 24, 75, 46, 8]
    print li7
    print plzd1(li7)
    print li8
    print plzd1(li8)
    print li9
    print plzd1(li9)
