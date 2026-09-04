totalSumN = 0
for i in range(2,354294):
    j = len(str(i)) -1
    sumN = 0
    while j >= 0:
        sumN += (i // 10**j % 10)**5
        j -= 1
    if sumN == i:
        totalSumN += sumN

print(totalSumN)

