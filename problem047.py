from math import *

def primeFactor( num, primesList ):
    factors = []
    for i in primesList:
        if num == 1:
            break
        else:
            if num%i == 0:
                count = 0
                while num%i == 0:
                    num = num/i
                    count += 1
                factors.append( i**count )
    return factors

def isPrime( num ):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1 ):
        if num%i == 0:
            return False
    return True

def allDiff( a, b, c, d ):
    e = a + b + c + d
    f = list(set(e))
    if len(f) == 16:
        return True
    else:
        return False

primesList = []
for i in range(1,1000):
    if isPrime(i):
        primesList.append(i)

for i in range(211, 1000000):
    if len(primeFactor(i, primesList)) != 4 and len(primeFactor(i+1, primesList)) != 4 and len(primeFactor(i+2, primesList)) != 4 and len(primeFactor(i+3, primesList)) != 4:
        continue
    else:
        if allDiff( primeFactor(i, primesList), primeFactor(i+1, primesList), primeFactor(i+2, primesList), primeFactor(i+3, primesList) ):
            print i
            break
         
