from collections import defaultdict
turn = 1
next_num = 0
prev_num = 0
numbers = defaultdict(int)
input = [0,8,15,2,12,1,4]


for i in input:
    numbers[i] = turn
    turn += 1 
    previous_num = i

while turn <= 30000000:
    if numbers[previous_num] == turn -1:
        next_num = 0
    else:
        next_num = (turn-1) - numbers[previous_num]
        numbers[previous_num] = turn -1
    if next_num not in numbers:
        numbers[next_num] = turn
    previous_num = next_num
    turn +=1

print(next_num)


