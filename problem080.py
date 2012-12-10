from math import *
from decimal import *

getcontext().prec = 105

def isIrrationalSqrt( num ):
    if num in [1,4,9,16,25,36,49,64,81,100]:
        return False
    else:
        return True

valueSum = 0
for i in range(2, 101):
    if isIrrationalSqrt( i ) == True:
        a = Decimal(i) ** Decimal('0.5')
        b = list( str(a) )
        valueSum += int(b[0])
        for c in range(2, 101):
            valueSum += int(b[c])

print( valueSum )
        
