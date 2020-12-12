f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

# initialise starting positions
ship = [90, 0, 0] # bearing, +N/-S, +E/-W
waypoint = [1, 10] # +N/-S, +E/-W

# execute instructions
for line in infile:
    instruction = line[0]
    distance = int(line[1:])
    ship_bearing = int(ship[0]) # 0=N, 90=E, 180=S, 270=W

    # move towards (relative) to waypoint X times
    if instruction == 'F':
        ship[1] = ship[1] + (waypoint[0] * distance)
        ship[2] = ship[2] + (waypoint[1] * distance)

    # move waypoint N/S/E/W
    elif instruction == 'N':
        waypoint[0] += distance
    elif instruction == 'S':
        waypoint[0] -= distance
    elif instruction == 'E':
        waypoint[1] += distance
    elif instruction == 'W':
        waypoint[1] -= distance

    # change bearing of waypoint
    elif instruction == 'L':
        if distance == 90:
            temp = waypoint[0]
            waypoint[0] = waypoint[1]
            waypoint[1] = - temp
        elif distance == 180:
            waypoint[0] = - waypoint[0]
            waypoint[1] = - waypoint[1]
        elif distance == 270:
            temp = waypoint[0]
            waypoint[0] = - waypoint[1]
            waypoint[1] = temp

    elif instruction == 'R':
        if distance == 90:
            temp = waypoint[0]
            waypoint[0] = - waypoint[1]
            waypoint[1] = temp
        elif distance == 180:
            waypoint[0] = - waypoint[0]
            waypoint[1] = - waypoint[1]
        elif distance == 270:
            temp = waypoint[0]
            waypoint[0] = waypoint[1]
            waypoint[1] = - temp

    # make the ships bearing correct and update the ship
    ship[0] = ship_bearing % 360
    #print("Ship:", ship)
    #print("Waypoint:", waypoint)

manhattan_distance = abs(ship[1]) + abs(ship[2])
print("Manhattan distance:", manhattan_distance)

# try this using switch statments at some point instead, or even make everything into function(s)
