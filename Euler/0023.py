import math
abundants = []
for number in range(28124):
    divisors = []
    divisor = 1
    while divisor <= math.sqrt(number):
        if number % divisor == 0:
            divisors.append(divisor)
            if divisor != 1 and number // divisor != divisor:
                divisors.append(number // divisor)
        divisor += 1
    dsum = 0
    for i in divisors: 
        dsum += i

    if dsum > number:
        abundants.append(number)

possibleNumbers = [True] * 28124
i = 0
while i < len(abundants):
    j = 0
    while j <= i: 
        number = abundants[i] + abundants[j]
        if number > 28123:
            break
        possibleNumbers[number] = False
        j += 1
    i += 1

abunsum = 0
i = 0
while i < len(possibleNumbers):
    
    if possibleNumbers[i]:
        abunsum += i
    i += 1

print(abunsum)
