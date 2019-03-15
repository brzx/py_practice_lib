import os

pt = os.path.abspath(os.curdir)
li = list(os.walk(pt))

with open('movewalks.txt','w') as f:
    for tp in li:
        a, _, c = tp
        f.write(str(a) + '\n')
        for it in c:
            f.write('    ' + str(it) + '\n')
