def returnFrac( iterCount ):
    if iterCount == 1:
        s = [1,2]
        return s
    else:
        for i in range( 2, iterCount+1 ):
            s = returnFrac( iterCount - 1 )
            t = [0,0]
            t[1] = s[0] + s[1]*2
            t[0] = s[1]
            return t

count = 0
for i in range(1, 1001):
    a = returnFrac( i )
    a[0] = a[0] + a[1]
    if ( len( str(a[0]) ) > len( str(a[1]) ) ):
        count += 1

print( count )
