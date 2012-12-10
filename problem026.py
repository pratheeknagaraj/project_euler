from decimal import Decimal

def getLongest( s, length, valueD ):
    if length <= 10:
        return -1
    else:
        currentMax = 0
        for j in range(0, 10):
            sub = s[j:j+4]
            dist = s.find(sub,j+1) - j
            if dist > currentMax:
                currentMax = dist
                if dist == 15:
                    print j, s.find(sub,j+1), sub
        return currentMax

currentMax = 6
valueD = 7
for i in range(2,1001):
    s = str(Decimal(1.0/i))[2:]
    length = len(s)
    if length <= valueD:
        continue
    longest = getLongest( s, length, valueD )
    if longest > currentMax:
        currentMax = longest
        valueD = i

print currentMax
print valueD
print Decimal(1.0/valueD)