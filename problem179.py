from math import *

def numOfDivisors( num ):
    count = 1
    if isPrime(num):
        return 2
    for i in primesList:
        miniCount = 1
        if num == 1:
            break
        elif num%i == 0:
            while num%i == 0:
                miniCount += 1
                num = int(num/i)
        count *= miniCount
    return count

def isPrime( num ):
    for i in range( 2, int(sqrt(num)) + 1 ):
        if num%i == 0:
            return False
    return True

primesList = []
primesList.append(2)
for i in range(3, 3333333, 2):
    if isPrime(i) == True:
        primesList.append(i)
        
count = 0
current = numOfDivisors(2)
for i in range(2, 10000001):
    if i%100000 == 0:
        print(i)
    s = numOfDivisors(i+1)
    if current == s:
        count += 1
    current = s

print( count )
