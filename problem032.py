import itertools

def left( num ):
    prodS = list(str(num))
    prodSLess = set(prodS)
    if len(prodS) != len(prodSLess) or '0' in prodS:
        return []
    else:
        nums = map(int, prodS)
        remain = []
        for i in range(1,10):
            if i not in nums:
                remain.append(i)
        return remain

def works( remain, num ):
    mult = 0
    perms = list(itertools.permutations(remain))
    for i in perms:
        if i[0]*(i[1]*1000+i[2]*100+i[3]*10+i[4]) == num:
            mult += num
            print str(i[0]) + " X " + str( (i[1]*1000+i[2]*100+i[3]*10+i[4]) ) + " = " + str(num)
            break
        if (i[0]*10+i[1])*(i[2]*100+i[3]*10+i[4]) == num:
            mult += num
            print str(i[0]*10+i[1]) + " X " + str( (i[2]*100+i[3]*10+i[4]) ) + " = " + str(num)
            break
    return mult
                
value = 0
for num in range(4200, 10000):
    remain = left( num )
    if len(remain) == 0:
        continue
    else:
        value += works( remain, num )

print value
