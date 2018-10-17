

def triangles(max):
    n = 1
    a = [1]
    while n<=max:
        if n==1:
            yield a
        elif n==2:
            yield a+a
        else:
            b = range(n)
            b[0] = 1
            b[1] = n - 1
            b[n-1] = 1
            b[n-2] = n - 1
            i = 2
            while i < n-2:
                b[i] = a[i-1]+a[i]
                i = i + 1
            a = b
            yield a
        n = n + 1

def tr1():
    n=1
    a=[1]
    while True:
        if n==1:
            yield a
        elif n==2:
            yield a+a
        else:
            b=list(range(n))
            b[0]=1
            b[1]=n-1
            b[n-1]=1
            b[n-2]=n-1
            i=2
            while i<n-2:
                b[i]=a[i-1]+a[i]
                i=i+1
            a=b
            yield a
        n=n+1

#if __name__ == '__main__':
#    for i in triangles(10):
#        print(i)
        
n = 0
results = []
for t in tr1():
    print(t)
    results.append(t)
    n = n + 1
    if n == 29:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('pass')
else:
    print('failed')