x = 2 ** 1000

x = str(x)


numbers = []
for i in x:
    numbers.append(int(i))

sum = 0 
for i in numbers:
    sum += i 

print(sum)