maxdiv = 0
maxlenght = 0
for divisor in range(1,1000):
    numlist = []
    x = 1
    remainders = []
    repetion = False
    start = 0
    while x != 0:
        x *= 10
        while x // divisor == 0:
            x *= 10
            numlist.append(0)

        newnum = x // divisor
        x %= divisor
        if x in remainders:
            repetion = True
            start =  remainders.index(x)
            break
        remainders.append(x)
        numlist.append(newnum)

    if len(numlist[start:]) > maxlenght:
        maxlenght = len(numlist[start:])
        maxdiv = divisor


print(maxlenght)
print(maxdiv)