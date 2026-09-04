
size = 1001

array = []
for i in range(size):
    array.append([0]*size)

x = int(len(array)//2)
y = int(len(array)//2)
array[y][x] = 1
incrementer = 2
first = True
last = False
while array[0][-1] == 0:
    #right
    while array[y+1][x] != 0 or first == True:
        if x == size-1:
            last = True
            break
        x += 1
        array[y][x] = incrementer
        incrementer += 1
        
        first  = False
    if last:
        break
    #down
    while array[y][x-1] != 0:
        y += 1
        array[y][x] = incrementer
        incrementer += 1
    #left
    while array[y-1][x] != 0:
        x -= 1
        array[y][x] = incrementer
        incrementer += 1
    #up
    while array[y][x+1] != 0:
        y -= 1
        array[y][x] = incrementer
        incrementer += 1


sum = -1

x = 0
y = 0
while x < size:
    sum += array[y][x]
    x += 1
    y += 1

x = size-1
y = 0
while x >= 0:
    sum += array[y][x]
    x -= 1
    y += 1

# # Convert 2D Array to String
# array_string = '\n'.join(['\t'.join(map(str, row)) for row in array])

# # Write to File
# with open(r'Euler\test.txt', 'w') as file:
#     file.write(array_string)

print(sum)