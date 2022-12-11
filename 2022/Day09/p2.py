f = open("example", "r")
input = f.read().splitlines()
input = [x.split(' ') for x in input ]  # split input on , to separate it easier

# build H and T grids
#        x y
xxx=15
yyy=15
H_pos  = [xxx,yyy]  # in centre of a large grid
T_pos = {1:[xxx,yyy], 2:[xxx,yyy], 3:[xxx,yyy], 4:[xxx,yyy], 5:[xxx,yyy], 6:[xxx,yyy], \
        7:[xxx,yyy], 8:[xxx,yyy], 9:[xxx,yyy]}
t_visited = []

def print_grid():
    # get size
    a, b = H_pos
    e = 0
    f = 0
    if t_visited != []:
        #print(max(t_visited))
        e, f = max(t_visited)
    size = abs(max(a,b,e,f))
    grid=[]
    
    for i in range(size+1):
        grid.append("#"*(size+1))
    
    for j in range(len(grid)):
        to_print = ""
        for i in range(len(grid[0])):
            #print(i, j, H_pos)
            if i == H_pos[0] and j == H_pos[1]:
                to_print += "H"
            elif i == T_pos[1][0] and j == T_pos[1][1]:
                to_print += "1"
            elif i == T_pos[2][0] and j == T_pos[2][1]:
                to_print += "2"
            elif i == T_pos[3][0] and j == T_pos[3][1]:
                to_print += "3"
            elif i == T_pos[4][0] and j == T_pos[4][1]:
                to_print += "4"
            elif i == T_pos[5][0] and j == T_pos[5][1]:
                to_print += "5"
            elif i == T_pos[6][0] and j == T_pos[6][1]:
                to_print += "6"
            elif i == T_pos[7][0] and j == T_pos[7][1]:
                to_print += "7"
            elif i == T_pos[8][0] and j == T_pos[8][1]:
                to_print += "8"
            elif i == T_pos[9][0] and j == T_pos[9][1]:
                to_print += "9"
            elif [i, j] in t_visited:
                to_print += "@"
            else:
                to_print += grid[j][i]
        print(to_print)
    
    

# function to see if T needs to move and to where
def check_tail(t, ox, oy):
    tx, ty = T_pos[t]
    if t == 1:
        hx, hy = H_pos
        print("H")
    else:
        hx, hy = T_pos[t-1]
        print("T")
    moves = 0
    
    # compare x
    print(tx-hx, ty-hy, T_pos, H_pos)
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
        move(t, [ox, oy])
        
    return moves


# function to move H
def move(knot, directon):
    global T_pos
    
    # special move for T knot
    if len(directon) == 2:
        if knot == 9 and (directon) not in t_visited:
            t_visited.append(directon)

        if knot == 1:  # if first knot use H
            print("H Moving T",str(knot), "to", directon)
            T_pos[knot][0] = directon[0]  # move T to last position of H
            T_pos[knot][1] = directon[1]  # move T to last position of H
            print("Checking", knot+1, "with", directon[0], directon[1])
            return check_tail(knot+1, directon[0], directon[1])

        else:  # if 2+ knot use previous tail
            print("T Moving T",str(knot), "to", T_pos[knot-1])
            T_pos[knot][0] = T_pos[knot-1][0]  # move T to last position of H
            T_pos[knot][1] = T_pos[knot-1][1]  # move T to last position of H

        print("T",str(knot), T_pos[knot])
        if knot != 9:
            print("Checking", knot+1, "with", T_pos[knot-1][0], T_pos[knot-1][1])
            return check_tail(knot+1, T_pos[knot-1][0], T_pos[knot-1][1])
        return 1
        
    # switch on what directon
    orig_x, orig_y = knot
    match directon:
        case "L":  # x -z
            knot[0] -= 1
        case "R":  # x +
            knot[0] += 1
        case "U":  # y +
            knot[1] += 1
        case "D":  # y -
            knot[1] -= 1
    print("H", knot)
    
    # need to check if T needs to move also if we moved H
    print("Checking 1 with", orig_x, orig_y)
    return check_tail(1, orig_x, orig_y)


# parse instructions
t_count = 0
for line in input:
    print("COMMAND:", line)
    
    # loop over each direction count N times
    for loop_count in range(int(line[1])):
        t_count += move(H_pos, line[0])
        print_grid()
        print()   
    
print()
print(t_count)
print(t_visited)
print(len(t_visited))