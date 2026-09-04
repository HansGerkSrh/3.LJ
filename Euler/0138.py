lenghts = []
import math

L = 1
while len(lenghts) < 12:
    
    bpos = ((-2 + math.sqrt(4 - 5 * (1-L*L))) /2.5)
    if bpos.is_integer() and bpos != 0:
        print(f"b pos: {bpos}")
        print(f"L : {L}\n")
        lenghts.append(L)

    bneg = ((2 + math.sqrt(4 - 5 * (1-L*L))) /2.5)
    if bneg.is_integer():
        print(f"b neg: {bneg}")
        print(f"L : {L}\n")
        lenghts.append(L)
    L += 1

sum = 0
for i in lenghts:
    sum += i

print(sum)