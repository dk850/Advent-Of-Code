f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

ship = [90, 0, 0] # bearing, +N/-S, +E/-W
for line in infile:
    instruction = line[0]
    distance = int(line[1:])
    ship_bearing = int(ship[0]) # 0=N, 90=E, 180=S, 270=W

    # move forwards
    if instruction == 'F':
        if ship_bearing == 90:
            ship[2] += distance
        elif ship_bearing == 270:
            ship[2] -= distance
        elif ship_bearing == 0:
            ship[1] += distance
        elif ship_bearing == 180:
            ship[1] -= distance

    # move N/S/E/W
    elif instruction == 'N':
        ship[1] += distance
    elif instruction == 'S':
        ship[1] -= distance
    elif instruction == 'E':
        ship[2] += distance
    elif instruction == 'W':
        ship[2] -= distance

    # change bearing
    elif instruction == 'L':
        ship_bearing -= distance
    elif instruction == 'R':
        ship_bearing += distance

    # make the ships bearing correct and update the ship
    ship[0] = ship_bearing % 360
    #print("Ship:", ship)

manhattan_distance = abs(ship[1]) + abs(ship[2])
print("Manhattan distance:", manhattan_distance)
