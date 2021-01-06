items = {}
counter = 0
trees = 0
with open ('YourFilePath/AdventOfCode2020/Puzzle3.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        (key,val) = (counter,line)
        items[counter] = val
        counter += 1
"""Part1 of the exercise
"""
# posy = 0
# posx = 0
# dictlength = range(len(items))
# stringlength = len(items[posy])
# for i in dictlength:
#     if posx >= stringlength:
#         posx = posx - stringlength

#     if (items[posy][posx]) == '#' :
#         trees += 1
#     posy += 1
#     posx += 3

# print(trees)

"""Part2 of the exercise
"""
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
#defining variables 
dictlength = range(len(items))
stringlength = len(items[0])
totaltrees = 1
rows = len(items)
#we set the loops we are going to iterate through
for i in range(len(slopes)):
    trees = 0
    increasey = slopes[i][1]
    increasex = slopes[i][0]
    posy = 0
    posx = 0
    #we iterate through the dictionary to check if we hit a tree or not
    
    for i in dictlength:
        if posy >= rows:
            break
        if posx >= stringlength:
            posx = posx - stringlength 
        if (items[posy][posx]) == '#' :
            trees += 1
        posy += increasey
        posx += increasex  
    print(trees)   
    totaltrees = totaltrees * trees
print(totaltrees)
