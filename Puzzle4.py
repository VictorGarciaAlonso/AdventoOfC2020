""" solution to first part of the puzzle
"""

# lista = [""]
# counter = 0
# valido = 0
# with open ('YourFilePathHere/Desktop/AdventOfCode2020/Puzzle4.txt') as f:
#     for line in f:
#         if  line.strip():
#             line = line.rstrip("\n")
#             lista[counter] = lista[counter] + ' ' + line
#         else:
#             lista.append("")
#             counter += 1
        

# expectedFields  = ["byr", "iyr" ,"eyr", "hgt" ,"hcl","ecl","pid"]
# for i in lista:
#     fields = 0
#     for j in expectedFields:
#         if j in i :
#             fields += 1
#     if fields == 7:
#         valido += 1

# print(valido)
import re

def validatefield(key,value):
    if key == "byr":
        try:
            if 1920 <= int(value) <= 2002:
                return True
            return False
        except:
            return False
    if key == "iyr":
        try:
            if 2010 <= int(value) <= 2020:
                return True
            return False
        except:
            return False        
    if key == "eyr":
        try:
            if 2020 <= int(value) <= 2030:
                return True
            return False
        except:
            return False    
    if key == "hgt":
        reghgt = re.compile('^1[5-9]\dcm|^[5-7]\din')
        if reghgt.search(value) != None:
            s = re.split('(\d+)',value)
            if s[2] == "in":
                if 59 <= int(s[1]) <=76:
                    return True
            elif s[2] ==  "cm":
                if 150 <= int(s[1]) <=193:
                    return True
            else:
                return False
        return False

    if key == "hcl":
        reghcl = re.compile('^#[0-9a-f]{6}')
        if reghcl.search(value) != None:
            return True
        return False
    if key == "ecl":
        if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
        return False
    if key == "pid":
        regpid = re.compile('^\d{9}$')
        if regpid.search(value) != None:
            return True
        return False
    if key == "cid":
        return True





"""Second part of the problem
"""
lista = [""]
counter = 0
valido = 0
expectedFields  = ["byr", "iyr" ,"eyr", "hgt" ,"hcl","ecl","pid"]
with open ('YourFilePathHere/Desktop/AdventOfCode2020/Puzzle4.txt') as f:
    for line in f:
        if  line.strip():
            line = line.rstrip("\n")
            lista[counter] = lista[counter] + ' ' + line
        else:
            lista.append("")
            counter += 1
dictlist = []
for i in lista:  #transform the list into a dictionary to better work

    s = i.split(' ')
    s = ' '.join(s).split()
    d = {h.split(':')[0]: h.split(':')[1] for h in s}
    dictlist.append(d)

for i in dictlist:
    fields = 7
    for j in expectedFields:
        if j not in i.keys():
            fields -= 1
    if fields == 7:
        for h in i.keys():
            if not validatefield(h,i[h]):
                fields -= 1
 
    if fields == 7:
        valido += 1
        for z in sorted (i.keys()) :
            print(z,i[z],end = ' ')  
        print("")
     


print(valido)
