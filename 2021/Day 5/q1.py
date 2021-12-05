def draw_arena(ruleset, arena):
    for row in arena:
        print(row)

    for rule in ruleset:
        print(rule)

        if rule[0][0] == rule[1][0]:  # x rule
            print("x")
        elif rule[0][1] == rule[1][1]:  # y rule
            print("y")
            arena[rule[0][0]][rule[0][1]] = 1
        break

    for row in arena:
        print(row)

f = open("testlist.txt", "r")
arena = f.read().splitlines()

# parse file
full_ruleset = []
for row in arena:
    rule = []
    rule.append([int(x) for x in row.split(' -> ')[0].split(',')])
    rule.append([int(x) for x in row.split(' -> ')[1].split(',')])
    full_ruleset.append(rule)

# part 1 only cares about vertical and horizontal lines so we only take into account the relevant rules
active_ruleset = []
for rule in full_ruleset:
    lhs = rule[0]
    rhs = rule[1]

    if (lhs[0] == rhs[0]) or (lhs[1] == rhs[1]):
        active_ruleset.append(rule)

# get the size of the arena from the largest value in the ruleset
flatten_list = [j for sub in active_ruleset for j in sub]
x_max = 0
y_max = 0
for entry in flatten_list:
    if int(entry[0]) > x_max:
        x_max = int(entry[0])
    if int(entry[1]) > y_max:
        y_max = int(entry[1])

# build the arena
arena = [ [0]*(x_max+1) for _ in range(y_max+1) ]
draw_arena(active_ruleset, arena)
