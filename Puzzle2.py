import collections
correct = 0
d = {}
with open ('YourFileHere/AdventOfCode2020/Puzzle2.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        (val,key) = line.split(":")  # we set the passwords as keys, assuming they are unique
        key = key.strip() 
        d[key] = val

"""
Part 1 of the problem

for i in d.keys() : # for all keys on the dict
    counter = 0
    for c in i: #for all letters on the key
        if c == d[i].split()[1]: # if the letter equals the one required on the pass
            counter += 1  #increase the counter of that letter 
    if counter in range(int(d[i].split()[0].split('-')[0]),(int(d[i].split()[0].split('-')[1]))+1): # if the counter is required in the pass
        correct += 1

"""


"""
Part 2 of the problem
"""
counter = 0
for i in d.keys() : # for all keys on the dict
    letter = d[i].split()[1]
    firstpos = int(d[i].split()[0].split('-')[0]) -1
    secondpos = int(d[i].split()[0].split('-')[1]) -1
    if (letter in i[firstpos]) or (letter in i[secondpos]):
        if (letter in i[firstpos]) and (letter in i[secondpos]):
            pass
        else:
            counter += 1 

print(counter)
