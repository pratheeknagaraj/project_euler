from math import *

def isPrime( n ):
    if n < 2:
        return False
    for i in range( 2, int(sqrt(n))+ 1 ):
        if n%i == 0:
            return False

    return True

def isTruncatable( n ):
    length = len(str(n))
    for i in range(0,length):
        test = int(str(n)[i:])
        if isPrime(test) == False:
            return False
    for i in range(length,0,-1):
        test = int(str(n)[:i])
        if isPrime(test) == False:
            return False
    return True

count = 0
num = 11
value = 0
while ( count != 11 ):
    if isTruncatable( num ):
        count += 1
        value += num
    num += 2

print value
