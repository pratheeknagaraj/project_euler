def isPandigital( nums ):
    newList = [ str(i) for i in nums ]
    combined = "".join(newList)
    combinedList = [int(i) for i in combined]
    combinedList2 = sorted(combinedList)
    if combinedList2 == [1,2,3,4,5,6,7,8,9]:
        return int(combined)
    else:
        return 0

highest = 123456789

## Numbers 1-2
for i in range(5000,9999+1):
    nums = []
    nums.append(i*1)
    nums.append(i*2)
    number = isPandigital(nums)
    if number > 0:
        if number > highest:
            highest = number
    else:
        continue

## Numbers 1-3
for i in range(100,333+1):
    nums = []
    nums.append(i*1)
    nums.append(i*2)
    nums.append(i*3)
    number = isPandigital(nums)
    if number > 0:
        if number > highest:
            highest = number
    else:
        continue

## Numbers 1-4
for i in range(25,33+1):
    nums = []
    nums.append(i*1)
    nums.append(i*2)
    nums.append(i*3)
    nums.append(i*4)
    number = isPandigital(nums)
    if number > 0:
        if number > highest:
            highest = number
    else:
        continue

## Numbers 1-5
for i in range(5,9+1):
    nums = []
    nums.append(i*1)
    nums.append(i*2)
    nums.append(i*3)
    nums.append(i*4)
    nums.append(i*5)
    number = isPandigital(nums)
    if number > 0:
        if number > highest:
            highest = number
    else:
        continue

## Numbers 1-6    
for i in range(3,3+1):
    nums = []
    nums.append(i*1)
    nums.append(i*2)
    nums.append(i*3)
    nums.append(i*4)
    nums.append(i*5)
    nums.append(i*6)
    number = isPandigital(nums)
    if number > 0:
        if number > highest:
            highest = number
    else:
        continue

## Numbers 1-9
for i in range(1,1+1):
    nums = []
    nums.append(i*1)
    nums.append(i*2)
    nums.append(i*3)
    nums.append(i*4)
    nums.append(i*5)
    nums.append(i*6)
    nums.append(i*7)
    nums.append(i*8)
    nums.append(i*9)
    number = isPandigital(nums)
    if number > 0:
        if number > highest:
            highest = number
    else:
        continue

## Result
print highest
