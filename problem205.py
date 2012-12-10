from math import *

## Case Peter
listP = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                for e in range(1,5):
                    for f in range(1,5):
                        for g in range(1,5):
                            for h in range(1,5):
                                for i in range(1,5):
                                    listP.append(a+b+c+d+e+f+g+h+i)

countP = []
totalP = pow(4,9)
for i in range(1,37):
    countP.append(listP.count(i))

print( countP )
print( "Done Peter" )

## Case Colin
listC = []
for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                                    listC.append(a+b+c+d+e+f)

countC = []
totalC = pow(6,6)
for i in range(1,37):
    countC.append(listC.count(i))

print( countC )
print( "Done Colin" )

## Total Probability
totalProb = 0
for i in range(36, 1, -1):
    valueSum = 0
    for j in range(i-1, 0, -1):
        valueSum += countC[j-1]
    totalProb += (valueSum/totalC)*(countP[i-1]/totalP)

print( totalProb )
