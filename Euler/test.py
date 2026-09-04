remainders = []
numlist = []
x = 1
while x != 0:
    x *= 10
    while x // 983 == 0:
        x *= 10
        numlist.append(0)
        
    newnum = x // 983
    x %= 983
    if x in remainders:
        repetion = True
        start =  remainders.index(x)
        break
    remainders.append(x)
    numlist.append(newnum)

    print(numlist)
    print(remainders)