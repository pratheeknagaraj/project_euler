from math import *
import operator

def rad( num ):
    product = 1
    for i in primesList:
        if num == 1:
            break
        elif num%i == 0:
            product *= i
            while num%i == 0:
                num = int(num/i)
    return product
            

def isPrime( num ):
    for i in range( 2, int(sqrt(num)) + 1 ):
        if num%i == 0:
            return False
    return True

primesList = []
for i in range(2, 100001):
    if isPrime(i) == True:
        primesList.append(i)

totalList = []
totalList.append([1,1])
for i in range(2,100001):
    totalList.append( [i, rad(i)] )

totalList = sorted( totalList, key=operator.itemgetter(1) )
print( totalList[10000-1] )
