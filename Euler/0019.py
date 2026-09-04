#1.Januar 1900
start = 0

from enum import Enum, auto

class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

startjahr  = 1900
endjahr = 2001
years = []

for i in range (0,endjahr-startjahr):
    jahr = startjahr + i
    schaltjahr = False
    if jahr % 4 == 0:
        schaltjahr = True
        if jahr % 100 == 0:  
            if jahr % 400 != 0: 
                schaltjahr = False
    years.append([])
    for j in range(12):
        years[i].append([])
        match Month(j+1):
            case Month.JANUARY| Month.MARCH| Month.MAY| Month.JULY| Month.AUGUST| Month.OCTOBER| Month.DECEMBER:
                monthlenght = 31 
            case Month.APRIL| Month.JUNE| Month.SEPTEMBER| Month.NOVEMBER:
                monthlenght = 30 
            case Month.FEBRUARY:
                if schaltjahr:
                    monthlenght = 29
                else:
                    monthlenght = 28

        if i == 0 and j == 0:
            startday = 0
        elif j == 0:
            startday = (years[i-1][-1][-1].value + 1) % 7
        else:
            startday = (years[i][j-1][-1].value + 1) % 7
        for k in range(monthlenght):
            years[i][j].append(Weekday((k + startday) % 7))   

# jahr = 1900
# i = 0
# while i < len(years):
#     j = 0
#     while j < len(years[i]):
#         k = 0
#         while k < len(years[i][j]):
#             print(f"{years[i][j][k].name} der {k+1}. im Monat: {Month(j+1).name} von Jahr: {jahr + i}")
#             k += 1
#         j += 1
#     i += 1

count = 0
i = 1
while i < len(years):
    j = 0
    while j < len(years[i]):
        if years[i][j][0] == Weekday.SUNDAY:
            count += 1
        j += 1
    i += 1

print(count)