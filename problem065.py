def returnFrac( current, iterCount ):
    if current == iterCount:
        a = [0,0]
        a[0] = 1
        a[1] = eList[current-2]
        return a
    else:
        a = [0,0]
        b = returnFrac( current + 1, iterCount )
        a[1] = eList[current-2]*b[1]+b[0]
        a[0] = b[1]
        return a
    

eList = []
for i in range(1,35):
    eList.append(1)
    eList.append(2*i)
    eList.append(1)

for i in range(100, 101):
    a = returnFrac( 2, i )
    b = [0,0]
    b[0] = 2*a[1]+a[0]
    b[1] = a[1]
    L = list(map(int, str(b[0])))
    valueSum = 0
    for i in L:
        valueSum += i
    print( valueSum )
    #print( str(b) + " : " + str( i ) )

