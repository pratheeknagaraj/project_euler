from math import *

def isRTriangle( a, b, c ):
    if c*c == a*a + b*b:
        return True
    else:
        return False

maxP = 0
maxCount = 1
for p in range( 5, 1001 ):
    print p
    count = 0
    a = 3
    while( a < (p - a)/2 ):
        for b in range( int( p/2.0 - a ) + 1, int( (p-a)/2.0 ) + 1 ):
             c = p - a - b
             if isRTriangle( a, b, c ):
                 count += 1
        a += 1
    if count > maxCount:
        maxCount  = count
        maxP = p
    

print str(maxP) + " :Done"
        
