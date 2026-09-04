numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

from collections import deque

def writenumber(number):
    word = deque([])

    wordand = False

    if number % 100 < 20 and number % 100 > 0:
        word.appendleft(numbers[number % 100])
        number -=  number % 100
        wordand = True
    
    for i in range(len(str(number))):
        digit = number // (10 ** i) % 10

        if i == 0 and digit != 0:
            word.appendleft(str(numbers[digit]))
            wordand = True
        if i == 1 and  digit != 0:  
            digit *= 10
            word.appendleft(str(numbers[digit]))
            wordand = True
        elif i == 2 and  digit != 0:
            if wordand:
                word.appendleft(str(numbers[digit]) + " hundred and")
            else:
                word.appendleft(str(numbers[digit]) + " hundred")

        elif i == 3 and  digit != 0:
            word.appendleft(str(numbers[digit]) + " thousand")

                

    returnword = ""
    for i in word:
        returnword += i + " "
    return returnword



count = 0
for i in range(1,1001):
    print(writenumber(i))
    numberword = writenumber(i)
    for letter in numberword:
        if letter != " ":
            count += 1

print(count)
