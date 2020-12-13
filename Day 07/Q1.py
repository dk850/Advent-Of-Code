def get_bag_info(rule):
    #print("Original Rule:", rule)
    bags = []

    # get master bag first in list
    rule = rule.split(" contain ")
    bags.append(rule[0][:-5])

    # add remaining bags and their count to the bags list
    rule = rule[1].split(",")
    for bag in rule:
        # remove any spaces at the start
        if bag[0] == " ":
            bag = bag[1::]
        if "no other bags" in bag:
            bags.append([0, "empty"])
            break
        # if there is only 1 bag it is formatted as "bag" not "bags"
        if bag[0] == "1":
            # also if it is the final bag it will have an extra space we need to remove
            if bag[-1] == ".":
                bags.append([int(bag[0]), bag[2:-5]])
            else:
                bags.append([int(bag[0]), bag[2:-4]])
        # if it is the final bag it will have an extra space we need to remove
        elif bag[-1] == ".":
            bags.append([int(bag[0]), bag[2:-6]])
        # if it contains no other bags
        else:
            bags.append([int(bag[0]), bag[2:-5]])

    # format [master_bag, [ [count, bag], [count, bag], ... ] ]
    # 0 = master bag, 1 = list of bags it contains (0..n)
    bags[1] = bags[1:]
    bags = bags[0:2]
    #print(bags)

    return bags

def check_bag_recursively(checking_bag):
    global global_possible_bags
    #print("Checking:", checking_bag)

    # base cases
    in_bag_count= 0
    for rule in bag_rules:

        # case #1, bag empty
        if( (checking_bag in rule[0]) & (rule[1][0][0] == 0) ):
            #print("Bag empty")
            global_possible_bags.append(checking_bag)
            return

        # case #2, bag not in any other bag
        for secondary in rule[1]:
            if checking_bag not in secondary:
                pass
            else:
                in_bag_count += 1
    if in_bag_count == 0:
        #print("Base bag")
        global_possible_bags.append(checking_bag)
        return

    for rule in bag_rules:
        for secondary in rule[1]:
            if checking_bag in secondary:
                check_bag_recursively(rule[0])
                global_possible_bags.append(checking_bag)

# Example1 = 4
f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

# make a list of all the bag rules
bag_rules = []
for rule in infile:
    bag_info = get_bag_info(rule)
    bag_rules.append(bag_info)

# for debug
if 0:
    print("Rules:")
    for rule in bag_rules:
        print(rule)
    print("\n")

goal_bag = "shiny gold"
global_possible_bags = []
# add every bag that shows up to the list
check_bag_recursively(goal_bag)

# sort out the global list, remove duplicates and the goal bag
single_bags = []
for bag in global_possible_bags:
    if (bag not in single_bags) & (bag != goal_bag):
        single_bags.append(bag)

print(len(single_bags))
