def fold_paper(paper, direction, position):
    # to simulate a fold we split the list into 2 based on the position and direction, then combine the lists
    if direction == "y":
        top = paper[:position]
        bottom = paper[position+1:]  # the line we fold on gets deleted and never has any dots on
        bottom.reverse()  # reverse the list to simulate us mirroring it as a flip/fold

        for y in range(len(bottom)):
            for x in range(len(bottom[0])):
                top[y][x] += bottom[y][x]  # add the elements of the reversed list to the top half to simulate a fold up

        return top


    else:  # x direction
        t_paper = list(map(list, zip(*paper)))  # transpose the list so we can easily 'fold' it like we did for y direction
        t_left = t_paper[:position]
        t_right = t_paper[position+1:]  # the line we fold on gets deleted and never has any dots on
        t_right.reverse()  # reverse the list to simulate us mirroring it as a flip/fold

        difference = abs(len(t_left) - len(t_right))  # need this for the physics of folding so we map the positions correctly
        for y in range(len(t_right)):
            for x in range(len(t_right[0])):
                t_left[y+difference][x] += t_right[y][x]  # add the elements of the reversed list to the top half to simulate a fold up

        left = list(map(list, zip(*t_left)))  # transpose the list again so it is the right way up
        return left



def display_grid(list_2d):
    for element in list_2d:
        print(element)



# parse and read in the highlighted positions and the instructions
f = open("input1.txt", "r")
input = f.read().splitlines()
input = [x.split(',') for x in input ]  # split input on , to separate it easier
positions_to_fill = [tuple(int(x) for x in x) for x in input if len(x) == 2]  # if the length of the element is 2 it is a position
fold_rules = [x[0].split('=') for x in input if len(x) == 1][1:]  # length 1 means it is a rule, split on the = and remove the empty line element
fold_rules = [(x[0][11:], int(x[1])) for x in fold_rules]  # get the horizontal fold (y|x) and the number as an int


# get the largest sizes so we can create a big enough list to represent the grid
x_max = 0
y_max = 0
for entry in positions_to_fill:
    if entry[0] > x_max:
        x_max = entry[0]
    if entry[1] > y_max:
        y_max = entry[1]

# build the representation of the paper
paper = [ [0]*(x_max+1) for _ in range(y_max+1) ]

# place the dots on the paper, reperesented as 1's
for rule in positions_to_fill:
    paper[rule[1]][rule[0]] = 1


# then we fold the paper based on all the fold rules - q1 only wants the first instruction executed
paper = fold_paper(paper, fold_rules[0][0], fold_rules[0][1])
for rule in fold_rules:
    paper = fold_paper(paper, rule[0], rule[1])
display_grid(paper)


# answer wants us to count the dots on the folded paper
dot_count = sum([len(list(x for x in x if x)) for x in paper])  # in the paper, only pay attention to values > 0, and sum the length of these lists
print("Dot count:", dot_count)
