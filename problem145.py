def isReversable( num ):
    str2 = str(num)
    len1 = len(str2)
    str3 = str2[::-1]
    num2 = int(str3)
    len2 = len(str(num2))
    if len1 != len2:
        return False
    sumNum = num + num2
    sumList = list(str(sumNum))
    for a in sumList:
        if int(a)%2 == 0:
            return False
    return True

count = 0
for i in range( 1, 1000000001 ):
    if i%1000000 == 0:
        print( i )
    if isReversable(i) == True:
        count += 1

print( count )

