def isprime(number):
    if number < 2:
        return False
    i = 2
    while i < number:
        if number % i == 0: 
            return False
        i += 1
    return True

bigestnum = 0
biga = 0
bigb = 0
for a in range(-1000,1000):
    for b in range(-1000,1001):
        n = 1
        primesum = 0
        while isprime(n * n + a * n + b):
            primesum += 1
            n += 1
        if primesum > bigestnum:
            bigestnum = primesum
            biga = a
            bigb = b

print(bigestnum)
print(biga * bigb)
print(biga)
print(bigb)
