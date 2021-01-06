""" First part of the problem.
"""

# lista = [""]
# counter = 0
# valido = 0
# questions = 0
# with open ('YourFilePath/Desktop/AdventOfCode2020/Puzzle6.txt') as f:
#     for line in f: #adding all the responses in to a list item
#         if  line.strip():
#             line = line.rstrip("\n")
#             lista[counter] = lista[counter] + ' ' + line
#             lista[counter].replace(" ", "")
#         else:
#             lista.append("") # if the line is a blank line, we increment the counter
#             counter += 1     # so we have the next item on a different list entry

# for i in lista:
#     i = i.replace(' ', '')
#     questions += len(set(i))
# print(questions)
      
"""Second part of the problem.
"""
lista = [""]
groups = {}
counter = 0
valido = 0
questions = 0
groups["grupo0"] = []   #initializing the dictionary for the answers (values) of every participant
with open ('YourFilePath/Desktop/AdventOfCode2020/Puzzle6.txt') as f:
    for line in f: #adding all the responses in to a dict item
        if  line.strip():
            line = line.rstrip("\n")
            groups["grupo" + str(counter)].append(line) #if we don't have a blank space, we add the value to the dictionary key (groupx)
        else:
            counter += 1     # so we have the next item on a different group entry, so we initialize the dictionary key to empty
            groups["grupo" + str(counter)] = []


for k in groups.keys(): #iterating over the groups 
    if len(groups[k]) == 1: #if ther eis only 1 person in the group, all the answers are valid
        questions = questions + len(groups[k][0])
    else:
        d = {} #initializing a dict to count repeated answers
        for i in groups[k]:
            if len(i) > 1: # if the strings are formed for more than 1 letter, we split them and count how many times the letter appears
                for j in i:
                    if j in d:
                        d[j] +=1
                    else:
                        d[j] = 1
            else: # if the letter only appears one, we check if it's on the dict already, and add it if not.
                if i in d:
                    d[i] +=1
                else:
                    d[i] = 1
        for value in d: #for the values of the letters, if it's equal to the number of people in the group,it's correct.
            if d[value] == len(groups[k]):
                questions = questions + 1                

print(questions)
