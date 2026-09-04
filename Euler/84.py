Square = [0] * 40

games = 1000
samples = 100000

import random

def roll_dice(count):
    x1 = random.randint(1,4)
    x2 = random.randint(1,4)
    if x1 == x2:
        count += 1
    else:
        count = 0
    return (x1,x2, count)
     
def Utilitys(field):
    if  27 < field < 40 or -1 < field < 12:
        field = 12
    else:
        field = 28
    return field

def Railway(field):
    if -1 < field < 5 or 34 < field < 40:
        field = 5
    elif 4 < field < 15:
        field = 15
    elif 14 < field < 25:
        field = 25 
    elif 24 < field < 35:
        field = 35
    return field 

def Goback(field):
    field -= 3
    if field < 0:
        field += 40
    return field

def pull_CH(index,field):
    global optionsCH

    if index == len(optionsCH): 
        index = 0

    result = optionsCH[index]
    if result == None:
        return None, index
    elif result == "RAIL":
        return Railway(field), index
    elif result == "UTILS":
        return Utilitys(field), index
    elif result == "GOBACK":
        return Goback(field), index
    else:
        return result, index

def pull_CC(index):
    global optionsCC
    if index == len(optionsCC): 
        index = 0
    return optionsCC[index], index

for j in range(games):

    optionsCH = [None,None,None,None,None,None,0,10,11,24,39,5,"RAIL","RAIL","UTILS","GOBACK"]
    random.shuffle(optionsCH)
    optionsCC = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,0,10]
    random.shuffle(optionsCC)

    field = 0
    count = 0
    chindex = 0
    ccindex = 0
    Square[0] += 1 
    for i in range(samples):
        x1, x2, count = roll_dice(count)
        if count == 3:
            field = 10
            Square[field] += 1 
            count = 0
            continue

        field += x1 + x2 
        field %= 40
        match field:
            case 30:
                field = 10
            case  7 | 22 | 36:
                result, chindex = pull_CH(chindex,field)
                chindex += 1
                if result != None:
                    field = result
            case 2 | 17 | 33:
                result, ccindex = pull_CC(ccindex)
                ccindex += 1
                if result != None:
                    field = result

        Square[field] += 1 

print("Numerisch Sortiert:\n")
j = 0
for i in Square:
    print(f"Feld Nr: {j} wurde {i} mal besucht")
    j += 1

i = 0
sum = 0
while i < len(Square):
    sum += Square[i]
    Square[i] = [Square[i], i]
    i += 1

Square.sort(reverse=True)
print("\nAbsteigend Sortiert:\n")
for i in Square:
        print(f"Feld Nr: {i[1]} wurde {i[0]} mal besucht Prozent: {i[0]/sum*100}%")