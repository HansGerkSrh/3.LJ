goal = 200
dividers = [200, 100, 50, 20, 10, 5, 2, 1]

coins= [0]*len(dividers)
i = 0
for divider in dividers:
    j = 0
    templist = []
    while j < goal / divider:
        templist.append(divider)
        j += 1
    coins[i] = templist
    i += 1

print(coins)
