lista = []

with open ('C:/Users/vgarciaalonso/Desktop/AdventOfCode2020/Puzzle1.txt') as f:
    lista = [int(line) for line in f]

s = set(lista)

for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if 2020 - lista[i] - lista[j] in s:
            print (lista[i], lista[j],2020 - lista[i] - lista[j])
            print(lista[i]*lista[j]*(2020 - lista[i] - lista[j]))
            break
    else: # if the look breaks because we reach a correct value, we need to break the outer loop too.
        continue
    break

