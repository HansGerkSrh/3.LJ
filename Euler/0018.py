input = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

input = input.splitlines()

i = 0
for line in input:
    input[i] = list(map(int, line.split()))
    i+= 1



def FindPath(j,data):
    if j < 0:  
        return data
    newdata = []
    for i in range(len(input[j])):
        if data[i][0] >= data[i + 1][0]:
            sum = input[j][i] + data[i][0]
            path = [input[j][i]] + data[i][1]
        else:
            sum = input[j][i] + data[i + 1][0]
            path = [input[j][i]] + data[i + 1][1]   
        newdata.append([sum, path])
    return FindPath(j - 1, newdata)

#Data[Index][Sum][Path]
data = []
for i in range(len(input[-1])):                       
    data.append([input[-1][i], [input[-1][i]]])        

result = FindPath(len(input)-2, data)

print("Sum: " + str(result[0][0]))
print("Path: " + str(result[0][1]))

