Range = 100000000

arr = [True] * Range

arr[0] = False
arr[1] = False
 
import math

for i in range(2,int(math.sqrt(Range))):
    if arr[i] == True:
        n = 2 
        while i * n < Range:
            arr[i*n] = False 
            n += 1

# j = 0
# for i in arr:
#     if i :
#         print(j)
#     j += 1 


primes = []
i = 0
j = 0
while i < 10001:
    if arr[j] == True:
        primes.append(j)
        i += 1
    j += 1

print(primes[-1])