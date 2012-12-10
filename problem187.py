from math import *
import numpy as np

def isPrime( num ):
    if num < 2:
        return False
    for i in range( 2, int(num**0.5)+ 1 ):
        if num%i == 0:
            return False
    return True

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def twoPrime( num, primeList ):
    if isPrime( num ):
        return False
    for i in primeList:
        if i > num/2:
            return False
        if num%i == 0:
            if isPrime( num/i ):
                return True
    return False
    
##primeList = []
##for i in range(1, 50000001 ):
##    if i%100000 == 0:
##        print i
##    if isPrime( i ):
##        primeList.append( i )
##
##print len(primeList)

primeList = primesfrom2to( 50000000 )
print len( primeList )

count= 0
for i in range(3, 100000001):
    if i%1000000 == 0:
        print i
    if twoPrime( i, primeList ):
        count += 1

print count
