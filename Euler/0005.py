num = 20
while True:
    condition = True
    for i in range(1,21):
        if num % i != 0:
            condition = False
            break
    if condition == True:
        print(num)
        break
    num += 20    