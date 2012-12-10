from math import *

def simplify( (num, denom) ):
    for i in range(2, num+1):
        if num%i == 0 and denom%i == 0:
            while( num%i == 0 and denom%i == 0 ):
                num = num/i
                denom = denom/i
    return ( num, denom )

def falseSimplify( (num, denom) ):
    sNum = str(num)
    sDenom = str(denom)
    eNum = num
    eDenom = denom
    if sNum[0] == sDenom[1]:
        eNum = num%10
        eDenom = denom/10
        return ( eNum, eDenom )
    elif sNum[1] == sDenom[0]:
        eNum = num/10
        eDenom = denom%10
        return ( eNum, eDenom )
    else:
        return ( 3, 2 )

nums = []
for i in range(11, 99):
    for j in range(i + 1, 100):
        if simplify(falseSimplify( (i, j) ) ) == simplify( (i, j) ) and (i,j) != simplify( (i, j) ):
            nums.append( (i,j) )

print "Number of Curious Fractions: " + str(len(nums))
numerator = 1
denominator = 1
for i in nums:
    numerator *= i[0]
    denominator *= i[1]

print simplify( (numerator, denominator) )[1]
