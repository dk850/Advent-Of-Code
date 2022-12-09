f = open("example", "r")
input = f.read().splitlines()
input = [x.split(' ') for x in input ]  # split input on , to separate it easier

# build H and T grids
#         x   y
H_pos = [100,100]  # in centre of a large grid
T_pos = [100,100]  # T starts on top of H
t_visited = []

# function to see if T needs to move and to where
def check_tail():
    tx, ty = T_pos
    hx, hy = H_pos
    moves = 0
    
    # compare row
    move_queue = []  # list of moves should be executed before executing, move at end, still count moves
    if tx-hx < -1:  # move x+
        move(T_pos, "R")
        if (tx, ty) not in t_visited:
            t_visited.append((tx, ty))
            moves += 1
    elif tx-hx > +1:
        move(T_pos, "L")
        if (tx, ty) not in t_visited:
            t_visited.append((tx, ty))
            moves += 1
            
        
    # compare column
    if ty-hy < -1:  # move x+
        move(T_pos, "U")
        if (tx, ty) not in t_visited:
            t_visited.append((tx, ty))
            moves += 1

    elif ty-hy > +1:
        move(T_pos, "D")
        if (tx, ty) not in t_visited:
            t_visited.append((tx, ty))
            moves += 1

    
    return moves


# function to move H
def move(knot, directon):
    # switch on what directon
    match directon:
        case "L":  # x -
            knot[0] -= 1
        case "R":  # x +
            knot[0] += 1
        case "U":  # y +
            knot[1] += 1
        case "D":  # y -
            knot[1] -= 1
    print("H" if knot == H_pos else "T", knot)
    
    # need to check if T needs to move also if we moved H
    if knot is H_pos:
        return check_tail()
    else:
        return 0



# parse instructions
t_count = 0
for line in input:
    print("COMMAND:", line)
    
    # loop over each direction count N times
    for loop_count in range(int(line[1])):
        print()   
        t_count += move(H_pos, line[0])
    
print(t_count)
print(t_visited)