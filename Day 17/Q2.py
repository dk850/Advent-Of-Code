def print_cube(cube):
    # for debugging to help with visualisation
    if type(cube) == list:
        print("Cube state:")
        for line in cube:
            print(line)
        print()

    else: # dictionary
        c_x = s_x = min(cube)[0]
        c_y = s_y = min(cube)[1]
        c_z = s_z = min(cube)[2]
        c_w = s_w = min(cube)[3]
        b_x = max(cube)[0]
        b_y = max(cube)[1]
        b_z = max(cube)[2]
        b_w = max(cube)[2]

        row = ""
        loop = True
        while loop:
            for key in cube:
                # build by rows
                if key[0] == c_x:
                    if key[1] == c_y:
                        if key[2] == c_z:
                            if key[3] == c_w:
                                row += cube[key] # add element to string if it is correct position

                                # if we have added last element in row, move down a column and reset row
                                if (c_x == b_x) and not (c_y == b_y) and not (c_w == b_w):
                                    c_x = s_x
                                    c_y += 1
                                    print(row)
                                    row = ""

                                # if we have added the last column, move up a z value and reset
                                elif (c_x == b_x) & (c_y == b_y) and not (c_w == b_w):
                                    c_x = s_x
                                    c_y = s_y
                                    c_z += 1
                                    print(row)
                                    row = ""
                                    print()

                                # if we have added last z move on to w increase
                                elif (c_x == b_x) & (c_y == b_y) & (c_z == b_z):
                                    c_x = s_x
                                    c_y = s_y
                                    c_z = s_z
                                    print(row)
                                    row = ""
                                    print()

                                    # if max w stop
                                    if c_w == b_w:
                                        loop = False
                                        break
                                    else:
                                        c_w += 1
                                else:
                                    c_x += 1
    return

def find_active_neighbours(individual_cube, big_cube):
    active_neighbours_count = 0

    # determine neighbours coordinates
    x = individual_cube[0]
    y = individual_cube[1]
    z = individual_cube[2]
    w = individual_cube[3]
    x_to_check = [x-1, x, x+1]
    y_to_check = [y-1, y, y+1]
    z_to_check = [z-1, z, z+1]
    w_to_check = [w-1, w, w+1]

    for inner_cube_key in big_cube:
        # check if coordinates are neighbours of our cube for each cube
        if (inner_cube_key[0] in x_to_check) & \
            (inner_cube_key[1] in y_to_check) & \
            (inner_cube_key[2] in z_to_check) & \
            (inner_cube_key[3] in w_to_check):

            # do not include the cube we are checking as a neighbour
            if inner_cube_key != individual_cube:

                # if the cube is on, add it to the count
                if big_cube[inner_cube_key] == '#':
                    active_neighbours_count += 1

    #print("Active neighbours count", active_neighbours_count)
    return active_neighbours_count

def cube_expansion_check(cube):
    # if there are any active cubes on the "side" of our working cube we return true to signifiy expansion
    s_x = min(cube)[0]
    s_y = min(cube)[1]
    s_z = min(cube)[2]
    s_w = min(cube)[3]
    b_x = max(cube)[0]
    b_y = max(cube)[1]
    b_z = max(cube)[2]
    b_w = max(cube)[3]

    # check edges of cube
    for inner_cube in cube:
        if (inner_cube[0] == s_x) | (inner_cube[0] == b_x) | \
            (inner_cube[1] == s_y) | (inner_cube[1] == b_y) | \
            (inner_cube[2] == s_z) | (inner_cube[2] == b_z) | \
            (inner_cube[3] == s_w) | (inner_cube[3] == b_w):
            if cube[inner_cube] == '#':
                #print("Cube requires expansion")
                return True
    return False

def expand_cube(big_cube):
    # we want to add an empty ('.') layer around our current grid
    bigger_cube = {}

    # get new mins and maxes for x, y, z
    s_x = min(big_cube)[0] -1
    s_y = min(big_cube)[1] -1
    s_z = min(big_cube)[2] -1
    s_w = min(big_cube)[3] -1
    b_x = max(big_cube)[0] +1
    b_y = max(big_cube)[1] +1
    b_z = max(big_cube)[2] +1
    b_w = max(big_cube)[3] +1
    #print("Min:", "("+str(s_x)+","+str(s_y)+","+str(s_z)+")", "Max:", "("+str(b_x)+","+str(b_y)+","+str(b_z)+")")

    for x in range(s_x, b_x+1):
        for y in range(s_y, b_y+1):
            for z in range(s_z, b_z+1):
                for w in range(s_w, b_w+1):
                    # fill in values we have from the cube we are expanding from first
                    if (x,y,z,w) in (k for k in big_cube):
                        bigger_cube[x, y, z, w] = big_cube[x, y, z, w]
                    # otherwise make it empty
                    else:
                        bigger_cube[x, y, z, w] = '.'
    #print(cube)
    #print_cube(bigger_cube)
    return bigger_cube

def do_the_cube_dance(big_cube):
    new_cube = {}

    # we have to evaluate each individual cube
    for cube in big_cube:
        active_neighbours_count = find_active_neighbours(cube, big_cube)
        #print(cube, big_cube[cube])

        # apply rule 1
        if big_cube[cube] == '#':
            if (active_neighbours_count == 2) | (active_neighbours_count == 3):
                new_cube[cube] = '#'
            else:
                new_cube[cube] = '.'

        # apply rule 2
        elif big_cube[cube] == '.':
            if active_neighbours_count == 3:
                new_cube[cube] = '#'
            else:
                new_cube[cube] = '.'

    #print(cube)
    #print_cube(new_cube)
    return(new_cube)

f = open("input.txt", "r")
infile = f.read().split('\n')
f.close()

#print_cube(infile)

# build cube in all inactive state except the input is z = 0
cube = {} # [x, y, z, w] : state
for x in range(len(infile[0])):
    for y in range(len(infile[0])):
        cube[y, x, 0, 0] = infile[x][y]

# question requires us to loop 6 times
for cycle in range(6):
    if cube_expansion_check(cube):
        cube = expand_cube(cube)
    #print_cube(cube)
    cube = do_the_cube_dance(cube)

#print_cube(cube)

sum = 0
for inner_cube in cube:
    if cube[inner_cube] == '#':
        sum += 1

print("Final sum of active cubes after 6 cycles:", sum)
