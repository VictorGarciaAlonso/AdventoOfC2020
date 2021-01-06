row = []
column = []
boardingPassList = []
with open ('YourFilepathHere/Desktop/AdventOfCode2020/Puzzle5.txt') as f:
    for line in f:
        row.append(line[0:7])
        column.append(line[7:10])
"""Solution to first puzzle
"""
# def returnrow(row): 
#     highseat = 127
#     lowseat = 0
#     for j in (row):     
#         if j == "B":
#             lowseat = lowseat + (((highseat - lowseat )// 2 ) + 1)
#         if j == "F":
#             highseat = lowseat + ((highseat - lowseat) // 2)
#     return(highseat)
# def returncol(col):
#     highseat = 7
#     lowseat = 0    
#     for j in (col):     
#         if j == "R":
#             lowseat = lowseat + (((highseat - lowseat )// 2 ) + 1)
#         if j == "L":
#             highseat = lowseat + ((highseat - lowseat) // 2)
#     return(highseat)

# highestValue = 0

# for i in range(len(column)):
#     temp = (returnrow(row[i]) * 8) + returncol(column[i])
#     if temp > highestValue :
#         highestValue = temp
# print(highestValue)
"""Solution to second puzzle
"""

def returnrow(row): 
    highseat = 127
    lowseat = 0
    for j in (row):     
        if j == "B":
            lowseat = lowseat + (((highseat - lowseat )// 2 ) + 1)
        if j == "F":
            highseat = lowseat + ((highseat - lowseat) // 2)
    return(highseat)
def returncol(col):
    highseat = 7
    lowseat = 0    
    for j in (col):     
        if j == "R":
            lowseat = lowseat + (((highseat - lowseat )// 2 ) + 1)
        if j == "L":
            highseat = lowseat + ((highseat - lowseat) // 2)
    return(highseat)

highestValue = 0

for i in range(len(column)):
    boardingPassList.append((returnrow(row[i]) * 8) + returncol(column[i]))
boardingPassList.sort() 
for i in range(len(boardingPassList)-1):
    if (boardingPassList[i+1] - boardingPassList[i]) > 1:
        print((boardingPassList[i])+1) 
        break
