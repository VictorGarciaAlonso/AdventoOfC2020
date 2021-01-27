items = []
with open ('yourfilepaht_/Puzzle13.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        items.append(line)

timestamp = items[0]
buses = items[1].split(",")
working_lines = {}
for item in buses:
    if item not in working_lines and item != "x":
        working_lines[item] = 0
        


for bus_line in working_lines.keys():
    time = int(bus_line) - (int(timestamp) % int(bus_line))
    working_lines[bus_line] = time

shortest_line = list(working_lines.keys())[0]

for bus_line in working_lines.keys():
    if working_lines[bus_line] < working_lines[shortest_line]:
        shortest_line = bus_line    

print(int(shortest_line) * int(working_lines[shortest_line]))
