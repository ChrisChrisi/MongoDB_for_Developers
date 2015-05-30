__author__ = 'Chris'

try:
    print 5 / 0
except Exception as e:
    print "exception: ", type(e), e

print 'after division on zero'
