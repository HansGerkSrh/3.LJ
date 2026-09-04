import math

sum = 0
i = 0
while True:
    sum += i
    j = 1
    devisors = []
    while j < math.sqrt(sum):
        if sum % j == 0:
            devisors.append(j)
            if sum // j not in devisors:
                devisors.append(sum // j)
        j += 1
    if len(devisors) > 500:
        print(sum)
        break
    i += 1
