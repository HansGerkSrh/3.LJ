a = 0
for b in range(1000):
    a = (-500000 + 1000* b) /(b -1000)
    if  a < b and a > 0 and a.is_integer(): 
        print(a)
        print(b)
        print(1000 - a - b )
        print(a*b * (1000 - a - b ))
