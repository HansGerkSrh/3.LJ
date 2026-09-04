import math
def functiond(number):
    sum = 0
    devisors = []
    i = 1
    while i < math.sqrt(number):
        if number % i == 0:
            devisors.append(int(i))
            if i != 1:
                devisors.append(int(number/i))
        i += 1

    for i in devisors:
        sum += i

    return sum


sum = 0
for i in range(10000):
    a = functiond(i)
    if functiond(a) == i and a != i:
        sum += i

print(sum)