from collections import defaultdict
items = []
DEFAULT_VALUE = "000000000000000000000000000000000000"
mem = defaultdict(lambda:DEFAULT_VALUE)
mask = ""
with open ('YourfileHere_Puzzle14.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        items.append(line)

"""First part of the puzzle
"""
# def changebits(mask,value):
#     new_value= []
#     ones_to_change = [i for i,x in enumerate(mask) if x == "1"]
#     zero_to_change = [i for i,x in enumerate(mask) if x == "0"]
#     for i,x in enumerate(value):
#         if i in ones_to_change:
#             new_value.append("1")
#         elif i in zero_to_change:
#             new_value.append("0")
#         else:
#             new_value.append(x)
#     new_value = "".join(new_value)
#     return(new_value)

# # print(items[2].split()[0].strip("mem[").strip("]")) #this is to obtain the memory address we will change 
# for instruction in items:
#     print(instruction)
#     if instruction.split()[0] == "mask":
#         mask = instruction.split()[2]
#         continue
#     else:
#         address = instruction.split()[0].strip("mem[").strip("]")
#         value = "{:036b}".format(int(instruction.split()[2]))
#         mem[address] = changebits(mask,value)

# suma = 0
# for i in mem.values():
#     suma += int(i,2)
# print(suma)



"""Second part of the puzzle
"""


def changebits(mask,value):
    new_value= []
    ones_to_change = [i for i,x in enumerate(mask) if x == "1"]
    floating_to_change = [i for i,x in enumerate(mask) if x == "X"]
    for i,x in enumerate(value):
        if i in ones_to_change:
            new_value.append("1")
        elif i in floating_to_change:
            new_value.append("X")
        else:
            new_value.append(x)
    new_value = "".join(new_value)
    return(new_value)


# it = [None] * 3 #for backtracking
# def permutations_item(value,iterables,count): Backtracking
#     if count == value:      
#         return
#     iterables[count] = 0
#     permutations_item(value,iterables,count + 1)
#     iterables[count] = 1
#     permutations_item(value,iterables,count + 1)    

def find_mask_Bits(mask):
    return [i for i, j in enumerate(mask) if j == "X"]

def generate_binary(n, l):
    if n == 0:
        return l
    else:
        if len(l) == 0:
            return generate_binary(n-1, ["0", "1"])
        else:
            return generate_binary(n-1, [i + "0" for i in l] + [i + "1" for i in l])
    
def modify_mask(mask,iter_item):
    count = 0
    temp_mask = list(mask)
    for item in find_mask_Bits(mask):
        temp_mask[item] = iter_item[count]
        count += 1
    temp_mask = "".join(temp_mask)
    return(temp_mask)  


for instruction in items:  # we pass through 
    #print(instruction)
    if instruction.split()[0] == "mask":
        mask = instruction.split()[2]
        continue
    else:
        iterated = [] # this is used to create a list with all the combinations of 0/1 of x lenght
        value = int(instruction.split()[2])  #this is the value that will be added to the dictionary address
        address = instruction.split()[0].strip("mem[").strip("]") # we retrieve the address the value should go
        address_bin =  "{:036b}".format(int(address))   #transformed in binary with lenght 36
        masked_address = changebits(mask,address_bin) # we do the mask transformation to the previously transforme value
        permutations = generate_binary(len(find_mask_Bits(masked_address)),iterated)  # generate the permutations each X can have
        for i in permutations: #for all the permutations generated, we put the value
            mem[int(modify_mask(masked_address,i),2)] = value    
 

suma = 0
for i in mem.values():
    suma += i
print(suma)
