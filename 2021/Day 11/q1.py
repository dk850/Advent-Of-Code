def all_increase(o_list, amount):
    o_list = [list(int(x)+int(amount) for x in x) for x in o_list]
    return o_list

def display_grid(list_2d):
    for a in list_2d:
        print(a)


# parse and read in the height map
f = open("../worklist.txt", "r")
octopi_input = f.read().splitlines()
octopi = [list(int(x) for x in x) for x in octopi_input]  # separate each string into its own int element in the list

print("Base grid:")
display_grid(octopi)
print()

steps_to_simulate = 2  # question requires 100 iterations
for _ in range(steps_to_simulate):
    octopi = all_increase(octopi, 1)  # step 1 is to increase all by 1
    display_grid(octopi)

    # step 2 is evaluate each level > 9


    print()
