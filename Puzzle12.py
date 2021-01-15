moves = []
direction = ""
path = {"E":0,"S":0,"W":0,"N":0}
amount = 0  
with open ('C:/Users/vgarciaalonso/Desktop/AdventOfCode2020/Puzzle12.txt') as f:
    for line in f:
        line = line.rstrip("\n")
        direction = line[0]
        amount = line[1:]
        moves.append((direction,amount))

"""
First part of the exercies
"""
# current_direction = "E"

# def rotate (current_direction,degrees): #to rotate, we move the list circularly by the module between the degrees and 90(only multiple of 90 degrees turn are expected)
#     directions = ["E","S","W","N"]
#     start = directions.index(current_direction)
#     new_dir = directions[(start + (degrees // 90 ) ) % 4]
#     return new_dir


# for items in moves:
#     d,l = items
#     if d=="F": #we move forward
#         path[current_direction] = path[current_direction] + int(l)
#     elif d=="R": #rotate to the right by degrees provided
#         current_direction = rotate(current_direction,int(l)) 
#     elif d=="L": #moving to the letf is the same as 360 - moving to the right (i.e : 90 to the left  = 270 to the right)
#         current_direction = rotate(current_direction,360-int(l))        
#     else:
#         path[d] = path[d] + int(l)     


# print(abs(path["E"] - path["W"]) + abs(path["N"] - path["S"]))

""" Second part of the exercise
"""
waypoint_dist = [10,1]
waypoint_dir = ["E","N"]

def rotate (current_direction,degrees): # we are rotating both points of the waypointby the same ammount 
    directions = ["E","S","W","N"]
    x,y = current_direction
    start_x = directions.index(x)
    start_y = directions.index(y)
    new_dir_x = directions[(start_x + (degrees // 90 ) ) % 4]
    new_dir_y = directions[(start_y + (degrees // 90 ) ) % 4]
    return([new_dir_x,new_dir_y]) 

def opposite(dir):  #calculating the opposite direction of a direction given
    if dir =="N":
        return("S")
    elif dir =="S":
        return("N")
    elif dir == "E":
        return("W")
    else:
        return("E")

def mod_waypoint(wdist,wdir,dir,units):  #operations with the waypoint
    if dir in wdir:  #if the direction we move is on the waypoint
        wdist[wdir.index(dir)] += units #we add the units moved
    else:
        tmp_val = wdist[wdir.index(opposite(dir))] - units #calculate how many units in the opposite direction we move
        if tmp_val > 0 :
            wdist[wdir.index(opposite(dir))] = tmp_val # if the current units - units moving on the opposite direction is >0 we keep the current direction
        else : #otherwise we change direction to the opposite, with the value calculated.
            wdist[wdir.index(opposite(dir))] =  abs(tmp_val)
            wdir[wdir.index(opposite(dir))]  =  dir
    return(wdist,wdir)


for items in moves:
    d,l = items

    if d=="F":
        for i in range(0,len(waypoint_dir)):
            path[waypoint_dir[i]] = path[waypoint_dir[i]] + (int(l) * waypoint_dist[i])

    elif d=="R":
        waypoint_dir = rotate(waypoint_dir,int(l)) 

    elif d=="L":
        waypoint_dir = rotate(waypoint_dir,360-int(l)) 

    else:
        waypoint_dist,waypoint_dir = mod_waypoint(waypoint_dist,waypoint_dir,d,int(l))   



print(abs(path["E"] - path["W"]) + abs(path["N"] - path["S"]))  #calculating manhattan point.
