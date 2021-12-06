def print_arena(arena):
    for row in arena:
        print(row)

def draw_arena(ruleset, arena):

    for rule in ruleset:  # loop over each rule
        print()
        print("Active rule:", rule)
        if rule[0][0] == rule[1][0]:    # x rule -> X values are the same; we modify row
            print("X rule")

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
            print("Y rule")

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
            arena[rule[0][0]][rule[0][1]] += 1

            arena[rule[1][0]][rule[1][1]] += 1
            print("non-rule")

        print_arena(arena)
        break


f = open("testlist.txt", "r")
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
