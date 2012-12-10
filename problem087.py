from math import *

def isPrime( num ):
    for i in range( 2, int(sqrt(num)) + 1 ):
        if num % i == 0:
            return False
    return True

maxNum = 50000000
primes = []
for i in range(2, int(sqrt(maxNum))+1):
    if isPrime(i):
        primes.append(i)

valid = []
for a in primes:
    if a > int(sqrt(maxNum))+1:
        break
    for b in primes:
        if b > int(pow(maxNum,1/3))+1:
            break
        for c in primes:
            if c > int(pow(maxNum,1/4))+1:
                break

            s = a*a + b*b*b + c*c*c*c
            if s < maxNum:
                valid.append(s)

x = set(valid)
print( len(x) )
