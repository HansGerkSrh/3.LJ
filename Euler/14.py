
numbers = {}

def Collatz(number):
    if number in numbers:
        return numbers[number]
    if number == 1:
        return 1
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    number = int(number)
    lenght = Collatz(number)
    numbers[number] = lenght
    return lenght + 1


#print(Collatz(837799,0))

maxlen = 0
maxstart = 0
for i in range(1,1000000):
    lenght = Collatz(i)
    if lenght > maxlen: 
        maxlen = lenght
        maxstart = i

print(maxstart)