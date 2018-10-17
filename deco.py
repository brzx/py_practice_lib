#!/usr/bin/env python

from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (
        ctime(), func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    print 'This is foo func.'
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()