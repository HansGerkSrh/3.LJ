fiblist = [0,1,1]
while len(str(fiblist[-1])) < 1000:
    fiblist.append(fiblist[-1] + fiblist[-2]) 
print(len(fiblist)-1)