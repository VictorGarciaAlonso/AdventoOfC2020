with open ('YourFilePath/Desktop/AdventOfCode2020/Puzzle9.txt') as f:
    lista = [int(line) for line in f]

"""  Part1
"""
windowsize = 25
solution1 = 0
for i in range(len(lista)- windowsize):
    s = set(lista[i:i+windowsize])
    target = lista[i+windowsize]
    counter = 0
    validtarget = False
    for z in s:
        if target - z in s:
            validtarget = True
    if validtarget == False:
        solution1 = target
        break


"""  Part2
"""



for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        temp = lista[i:j]
        if sum(temp) == solution1:
            print(min(temp),max(temp))
            print(min(temp)+max(temp))
            break
    else:
        continue # this break is only reached if the condition inside the if is never reached in the for loop
    break
