stack = {}
counter = 0
ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}
with open ('YourFilePath/Desktop/AdventOfCode2020/Puzzle8.txt') as f:
    for line in f: 
        line.strip()
        line = line.rstrip("\n")
        stack[counter] = line.split()
        counter +=1
"""first part


instructions = set()
accumulator = 0
pos = 0
while pos not in instructions:
    instructions.add(pos)
    if stack[pos][0] == "nop":
        pos +=1
    elif stack[pos][0] == "acc":
        accumulator = ops[stack[pos][1][0]] (accumulator,int(stack[pos][1][1:]))
        pos +=1
    elif stack[pos][0] == "jmp":
        pos = ops[stack[pos][1][0]] (pos,int(stack[pos][1][1:]))
print(accumulator)
"""


"""
second part 
"""

def validate(pila) :        
    instructions = set()
    accumulator = 0
    pos = 0
    while pos not in instructions:
        if pos == len(stack.keys()):
            return True
        instructions.add(pos)
        if stack[pos][0] == "nop":
            pos +=1
        elif stack[pos][0] == "acc":
            accumulator = ops[stack[pos][1][0]] (accumulator,int(stack[pos][1][1:]))
            pos +=1
        elif stack[pos][0] == "jmp":
            pos = ops[stack[pos][1][0]] (pos,int(stack[pos][1][1:]))
    return False


for i in stack.keys():
    if stack[i][0] == "jmp":
        stack[i][0] = "nop"
        if validate(stack):
            break
        else:
            stack[i][0] = "jmp"

    elif stack[i][0] == "nop":
        stack[i][0] = "jmp"
        if validate(stack):
            break
        else:
            stack[i][0] = "nop"

def calculateAcc(pila):
    instructions = set()
    accumulator = 0
    pos = 0
    while pos not in instructions and pos < len(pila):
        instructions.add(pos)
        if stack[pos][0] == "nop":
            pos +=1
        elif stack[pos][0] == "acc":
            accumulator = ops[stack[pos][1][0]] (accumulator,int(stack[pos][1][1:]))
            pos +=1
        elif stack[pos][0] == "jmp":
            pos = ops[stack[pos][1][0]] (pos,int(stack[pos][1][1:]))
    print(accumulator)


calculateAcc(stack)      
