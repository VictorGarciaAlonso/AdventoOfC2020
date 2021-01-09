lines = 0
d = {}
 

with open ('C:/Users/vgarciaalonso/Desktop/AdventOfCode2020/Puzzle11.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        rows = 0
        for letter in line:
            d[lines,rows] = letter
            rows += 1
        lines += 1

#adjacency for first part
def adjacent(tupla,dic):
    seats = []
    currentline,currentrow = tupla
    for i in range(currentline -1,currentline + 2):
        for j in range(currentrow -1,currentrow + 2):
            if (i,j) in dic.keys() and (i,j) != tupla and dic[(i,j)] != ".":
                seats.append((i,j))
    return(set(seats))                

#adjacency for second part
def firstVisible(tupla,dict,linesize,rowsize):
    seats = []
    posline,posrow = tupla
    for i in range(posline,-1,-1): # move up
        if d[(i,posrow)] != "." and (i,posrow) != tupla :
            seats.append((i,posrow))
            break
    for i in range(posrow,-1,-1): # move left
        if d[(posline,i)] != "." and (posline,i) != tupla:
            seats.append((posline,i))
            break
    for i in range(posline,linesize):# move down
        if d[(i,posrow)] != "." and (i,posrow) != tupla:
            seats.append((i,posrow))
            break
    for i in range(posrow,rowsize): #move right
        if d[(posline,i)] != "." and (posline,i) != tupla:
            seats.append((posline,i))
            break  
    # doing corners 
    l,r = tupla
    while  linesize-1 >= l >= 0 and  rowsize-1 >= r >= 0:  # corner up left
        if d[l,r] != "." and (l,r) != tupla :  
            seats.append((l,r))
            break
        l -=1
        r -=1
            
    l,r = tupla
    while linesize-1 >= l >= 0 and  rowsize-1 >= r >= 0:#corner down right
        if d[l,r] != "." and (l,r) != tupla :  
            seats.append((l,r))
            break
        l +=1
        r +=1
            
    l,r = tupla
    while linesize-1 >= l >= 0 and  rowsize-1 >= r >= 0:#corner up right
        if d[l,r] != "." and (l,r) != tupla :  
            seats.append((l,r))
            break
        l -=1
        r +=1
            
    l,r = tupla
    while linesize-1 >= l >= 0 and  rowsize-1 >= r >= 0:#corner up right
        if d[l,r] != "." and (l,r) != tupla :  
            seats.append((l,r))
            break
        l +=1
        r -=1            
    return(seats)
def occupy(tupla,dic,adjacentes):
    ocupados = 0
    for i in adjacentes:
        if dic[i] == "#" :
            ocupados += 1
    if  ocupados >= 1 :
        return(False)
    else:
        return(True)

def empty(tupla,dic,adjacentes):
    ocupados = 0
    for i in adjacentes:
        if dic[i] == "#" :
            ocupados += 1
    if  ocupados >= 5:
        return(True)
    else:
        return(False)       


""" First part 
"""
# emptyAux = [""]
# occupyAux = [""]

# while emptyAux != [] or occupyAux != []:
#     emptyAux = []
#     occupyAux = []
#     for i in d.keys():
#         if d[i] == "L":
#             adyacences = adjacent(i,d)
#             if occupy(i,d,adyacences):
#                 occupyAux.append(i)    
#         elif d[i] == "#":
#             adyacences = adjacent(i,d)
#             if empty(i,d,adyacences):
#                 emptyAux.append(i)
#     for k in emptyAux:
#         d[k] = "L" 
#     for k in occupyAux:
#         d[k] = "#"       



# """Second part
# """
emptyAux = [""]
occupyAux = [""]

while emptyAux != [] or occupyAux != []:
    emptyAux = []
    occupyAux = []
    for i in d.keys():
        if d[i] == "L":
            adyacences = firstVisible(i,d,lines,rows)
            if occupy(i,d,adyacences):
                occupyAux.append(i)    
        elif d[i] == "#":
            adyacences = firstVisible(i,d,lines,rows)
            if empty(i,d,adyacences):
                emptyAux.append(i)
    for k in emptyAux:
        d[k] = "L" 
    for k in occupyAux:
        d[k] = "#" 

occupiedSeats = 0
for i in d.keys():
    if d[i] == "#":
        occupiedSeats += 1

print(lines,rows)
for i in range(0,rows-1):
    for j in range(0,lines-1):
        print(d[(i,j)],end ="")
    print("")

# print(d)
print(occupiedSeats)
