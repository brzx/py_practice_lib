import sys, os


try:
    if sys.argv[1] is not None:
        print 'Command 1 is', sys.argv[1]
except:
    print 'No command input!'

















'''
print 'sys.argv[0] =', sys.argv[0]
pathname = os.path.dirname(sys.argv[0])
print 'path =', pathname
print 'full path =', os.path.abspath(pathname)
'''