def print_arena(arena):
    for row in arena:
        print(row)



def draw_arena(ruleset, arena):
    for rule in ruleset:  # loop over each rule

        # x rule -> X values are the same; we modify row
        if rule[0][0] == rule[1][0]:

            # get start and end of coordinate to draw from
            x_value = rule[0][0]
            y_start = rule[0][1]
            y_end   = rule[1][1]
            if y_start > y_end:  # make sure they are in order of smallest -> largest
                temp = y_start
                y_start = y_end
                y_end = temp

            # draw it on the grid
            for pos in range(y_start, y_end+1):
                arena[pos][x_value] += 1


        elif rule[0][1] == rule[1][1]:  # y rule -> Y values are the same; we modify column

            # get start and end of coordinate to draw from
            y_value = rule[0][1]
            x_start = rule[0][0]
            x_end   = rule[1][0]
            if x_start > x_end:  # make sure they are in order of smallest -> largest
                temp = x_start
                x_start = x_end
                x_end = temp

            # draw it
            for pos in range(x_start, x_end+1):
                arena[y_value][pos] += 1


        else:  # otherwise we have a diagonal rule
            leftern = -1    # leftern most coordinate will be either rule 0 or rule 1
            direction = -1  # direction of movement will be 0 for down and 1 for up

            # find leftern most rule
            if rule[0][0] < rule[1][0]:  # if rule 0 x value is smaller than rule 1 x value, we have the leftern most rule
                leftern = 0
            else:
                leftern = 1

            # find the direction we need to go in
            if rule[leftern][1] > rule[0 if leftern == 1 else 1][1]:  # if our leftern rule has a larger Y then we need to go UP
                direction = 1  # up
            else:
                direction = 0  # down

            # draw the path
            position = [rule[leftern][0], rule[leftern][1]]  # x, y of lefternmost rule
            while 1:  # we dont know need to know the length of the line, can just loop until we reach the end
                arena[position[1]][position[0]] += 1  # draw current position

                # increase the position
                if direction == 1:  # up direction
                    position[0] += 1
                    position[1] -= 1

                else:  # down direction
                    position[0] += 1
                    position[1] += 1

                # break if we have reached the other rule, meaning we have drew the whole line
                if position == [rule[0 if leftern == 1 else 1][0], rule[0 if leftern == 1 else 1][1]]:
                    arena[position[1]][position[0]] += 1  # draw position
                    break



f = open("input1.txt", "r")
arena = f.read().splitlines()

# parse file
full_ruleset = []
for row in arena:
    rule = []
    rule.append([int(x) for x in row.split(' -> ')[0].split(',')])
    rule.append([int(x) for x in row.split(' -> ')[1].split(',')])
    full_ruleset.append(rule)

# get the size of the arena from the largest value in the ruleset
flatten_list = [j for sub in full_ruleset for j in sub]
x_max = 0
y_max = 0
for entry in flatten_list:
    if int(entry[0]) > x_max:
        x_max = int(entry[0])
    if int(entry[1]) > y_max:
        y_max = int(entry[1])

# build the arena
arena = [ [0]*(x_max+1) for _ in range(y_max+1) ]
draw_arena(full_ruleset, arena)
#print_arena(arena)


# determine how many lines overlap (how many >1s there are)
count = 0
for row in arena:
    for element in row:
        if element > 1:
            count += 1
print()
print("Overlaps:", count)
