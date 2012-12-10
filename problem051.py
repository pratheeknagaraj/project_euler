from math import *
from itertools import *
import sys

def isPrime( num ):
    for i in range(2, int(sqrt( num )) + 1):
        if num%i == 0:
            return False
    return True

def getPossible( pos, num ):
    count = 0
    digits = int_to_list(num)
    for i in range(0,10):
        for j in pos:
            digits[j] = i
        if isPrime( list_to_int( digits ) ):
            count += 1
    if count == 8:
        print pos
    return count

def int_to_list(i):
    return [int(x) for x in str(i).zfill(len(str(i)))]

def list_to_int(l):
    return int("".join(str(x) for x in l))
    

found = False
start = 3
num = start
while found == False:
    if isPrime( num ):
        length = len(str(num))
        arr = [x for x in range(1, length)]
        for i in range(1,length-2):
            pos = list(set(combinations( arr, i )))
            for j in pos:
                value = getPossible( j, num )
                if value == 9:
                    found = True
                    print num
                    sys.exit(0)
    if num%100000 == 1:
        print num
    num += 2

print num - 2



