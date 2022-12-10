f = open("input", "r")
input = f.read().splitlines()
input = [x.split(' ') for x in input ]  # split input on , to separate it easier

# build H and T grids
#         x   y
H_pos = [100,100]  # in centre of a large grid
T_pos = [100,100]  # T starts on top of H
t_visited = []

def print_grid():
    # get size
    a, b = H_pos
    c, d = T_pos
    e = 0
    f = 0
    if t_visited != []:
        #print(max(t_visited))
        e, f = max(t_visited)
    size = abs(max(a,b,c,d,e,f))
    grid=[]
    
    for i in range(size+1):
        grid.append("#"*(size+1))
    
    for j in range(len(grid)):
        to_print = ""
        for i in range(len(grid[0])):
            #print(i, j, H_pos)
            if i == H_pos[0] and j == H_pos[1]:
                to_print += "H"
            elif i == T_pos[0] and j == T_pos[1]:
                to_print += "T"
            elif [i, j] in t_visited:
                to_print += "@"
            else:
                to_print += grid[j][i]
        print(to_print)
    
    

# function to see if T needs to move and to where
def check_tail(ox, oy):
    tx, ty = T_pos
    hx, hy = H_pos
    moves = 0
    
    # compare x
    #print(tx-hx, ty-hy, T_pos, H_pos)
    if tx-hx < -1:
        moves = 1
    elif tx-hx > +1:
        moves = 1
            
    # compare y
    if ty-hy < -1:
        moves = 1
    elif ty-hy > +1:
        moves = 1

    if moves != 0:  # if we need to move, move to last position of h
        move(T_pos, [ox, oy])
        
    return moves


# function to move H
def move(knot, directon):
    global T_pos
    orig_x, orig_y = knot
    
    # special move for T knot
    if len(directon) == 2:
        print("Moving T to", directon)
        if (directon) not in t_visited:
            t_visited.append(directon)
        T_pos[0] = directon[0]  # move T to last position of H
        T_pos[1] = directon[1]  # move T to last position of H
        print("T", knot)
        return 1
        
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
    print("H", knot)
    
    # need to check if T needs to move also if we moved H
    #if knot is H_pos:
    return check_tail(orig_x, orig_y)
    #else:
    #    return 0



# parse instructions
t_count = 0
for line in input:
    print("COMMAND:", line)
    
    # loop over each direction count N times
    for loop_count in range(int(line[1])):
        t_count += move(H_pos, line[0])
        #print_grid()
        print()   
    
print()
print(t_count)
print(t_visited)
print(len(t_visited))