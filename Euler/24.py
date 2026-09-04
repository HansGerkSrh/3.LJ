permutationslist = []
def permutations(a, size):
    if size == 1:
        permutationslist.append(tuple(a))
        return
    for i in range(size):
        permutations(a, size - 1)
        if size % 2 == 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]


a = [0,1,2,3,4,5,6,7,8,9]
permutations(a,len(a))

numberslist = []

for i in permutationslist: 
    k = 0
    number = 0
    for j in range(len(i)-1,-1,-1):
        number += i[k] * 10 ** j
        k += 1 
    numberslist.append(number)

numberslist.sort()
print(numberslist[999999])