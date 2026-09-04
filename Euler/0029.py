a = 2
b = 2

products = []

lenght = 100
while a <= lenght:
    b =2
    while b <= lenght: 
        psum = a 
        i = 1
        while i < b:
            psum *= a  
            i += 1
        if psum not in products:
            products.append(psum)
        b += 1
    a += 1

print(len(products))