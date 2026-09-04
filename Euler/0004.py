def ispali(num):
    num =str(num)
    i = 0
    j = len(num) -1
    while i < len(num) // 2:
        if num[i] != num[j]:
            return False
        j -= 1
        i += 1
    return True

largest = 0
nums = ()
for i in range(1000):
    for j in range(1000):
        num = i * j 
        if ispali(num):
            if num > largest:
                largest = num
                nums = (i,j)
            

print(largest)
print(nums)
