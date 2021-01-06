lines = []
bags = {}
target = "shinygold"
counter = 0
with open ('YourFilePath/Desktop/AdventOfCode2020/Puzzle7.txt') as f:
    for line in f: 
        line.strip()
        line = line.rstrip("\n")
        lines.append(line)
"""part 1 of the problem
"""
# for item in lines: #creating the topology where vertices are bags and nodes are the bags they contain
#     temp = item.split()
#     src = "".join(temp[0:2])
#     dst = []
#     if temp[-3] == "no" or temp[-3] == "contains" :
#         bags[src] = dst
#     else:
#         for i in range(5,len(temp),4):
#             dst.append("".join(temp[i:i+2]))
#         bags[src] = dst


# def findpaths(graph,start,target,path=[]): #function to move through the graph 
#     path = path + [start]
#     if start == target: #if it's the target, we return the whole path
#         return [path]
#     paths = []
#     for node in graph[start]: #for all the nodes inside the vertice
#         if node not in path: # if we don't already have that node in the path
#             newpaths = findpaths(graph, node, target, path) #we recursively run the node
#             for newpath in newpaths:
#                 paths.append(newpath)
#     return paths

# for i in bags.keys():
#     if findpaths(bags,i,target,path=[]) != []:
#         counter += 1
# print(counter-1) #is one less as the target will be counted as 1 path


"""part 2 of the problem
"""       
for item in lines: #creating the topology where vertices are bags and nodes are the bags they contain (and how many)
    temp = item.split()
    src = "".join(temp[0:2])
    dst = []
    if temp[-3] == "no" or temp[-3] == "contains" :
        bags[src] = dst
    else:
        for i in range(5,len(temp),4):
            dst.append("".join(temp[i-1:i+2]))
        bags[src] = dst

def size(bolsa): #we run through the keys in the first item.
    tam = 1
    for i in bags[bolsa]:
        tam += int(i[0])*size(i[1:])
    return(tam)

print(size(target)-1)


 
