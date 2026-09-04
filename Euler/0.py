sum = 0
for i in range(716000):
    square = i * i 
    if square % 2 != 0: 
        sum += square

print(sum)