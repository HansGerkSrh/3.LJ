product = 1
for i in range(1,101):
    product *= i

sum = 0

for i in str(product):
    sum += int(i)

print(sum)