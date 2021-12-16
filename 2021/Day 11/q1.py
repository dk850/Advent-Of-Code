def all_increase(o_list, amount):
    o_list = [list(int(x)+int(amount) for x in x) for x in o_list]
    return o_list


def flash(grid, position_x, position_y):
    # determine our position in easy to read variables
    left_side  = 1 if position_x == 0 else 0
    right_side = 1 if position_x == (len(grid[position_x]) - 1) else 0
    top_row    = 1 if position_y == 0 else 0
    bottom_row = 1 if position_y == (len(grid) - 1) else 0

    # safely add 1 to addressable positions on the grid
    if left_side:
        if top_row:
            grid[y][x+1]   += 1
            grid[y+1][x]   += 1
            grid[y+1][x+1] += 1
        elif bottom_row:
            grid[y][x+1]   += 1
            grid[y-1][x]   += 1
            grid[y-1][x+1] += 1
        else:
            grid[y][x+1]   += 1
            grid[y+1][x]   += 1
            grid[y+1][x+1] += 1
            grid[y-1][x]   += 1
            grid[y-1][x+1] += 1

    elif right_side:
        if top_row:
            grid[y][x-1]   += 1
            grid[y+1][x]   += 1
            grid[y+1][x-1] += 1
        elif bottom_row:
            grid[y][x-1]   += 1
            grid[y-1][x]   += 1
            grid[y-1][x-1] += 1
        else:
            grid[y][x-1]   += 1
            grid[y+1][x]   += 1
            grid[y+1][x-1] += 1
            grid[y-1][x]   += 1
            grid[y-1][x-1] += 1
    else:
        if top_row:
            grid[y][x-1]   += 1
            grid[y][x+1]   += 1
            grid[y+1][x]   += 1
            grid[y+1][x-1] += 1
            grid[y+1][x+1] += 1
        elif bottom_row:
            grid[y][x-1]   += 1
            grid[y][x+1]   += 1
            grid[y-1][x]   += 1
            grid[y-1][x-1] += 1
            grid[y-1][x+1] += 1
        else:
            grid[y][x-1]   += 1
            grid[y][x+1]   += 1
            grid[y-1][x]   += 1
            grid[y-1][x-1] += 1
            grid[y-1][x+1] += 1
            grid[y+1][x]   += 1
            grid[y+1][x-1] += 1
            grid[y+1][x+1] += 1

    return


def display_grid(list_2d):
    for element in list_2d:
        print(element)



# parse and read in the octopus values
f = open("input1.txt", "r")
octopi_input = f.read().splitlines()
octopi = [list(int(x) for x in x) for x in octopi_input]  # separate each string into its own int element in the list

print("Base grid:")
display_grid(octopi)

steps_to_simulate = 100  # question requires 100 iterations
flashes_count = 0
for _ in range(steps_to_simulate):

    # step 1 is to increase all by 1
    octopi = all_increase(octopi, 1)

    # step 2 is evaluate each level > 9
    flashed = []
    to_loop = 1
    while to_loop:
        to_loop = 0  # assume this is the last loop

        # loop over the whole grid to get x, y positions
        for y in range(len(octopi)):
            for x in range(len(octopi[0])):
                position = (x, y)

                if (octopi[y][x] > 9) and (position not in flashed):  # check it hasnt already flashed
                    flash(octopi, x, y)
                    flashed.append(position)
                    to_loop = 1  # we must loop again to check this flash did not impact any other octopus

    # step 3 is to reset any flashed octopi to 0
    for octo_pos in flashed:
        octopi[octo_pos[1]][octo_pos[0]] = 0

    # answer wants us to track the number of flashes
    flashes_count += len(flashed)

print()
print("Final grid after", steps_to_simulate, "iterations:")
display_grid(octopi)
print("Flashes count:", flashes_count)
