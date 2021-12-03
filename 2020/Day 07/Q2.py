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

def sum_inner_bags_recursively(checking_bag):
    #print("Checking bag:", checking_bag)

    # base case is bag empty
    for rule in bag_rules:
        if( (checking_bag in rule[0]) & (rule[1][0][0] == 0) ):
            #print("Empty bag")
            return (int(1), False) # this false signifies not to add the bag to the sum later on

    # find the rule that relates to the bag we need to check
    for rule in bag_rules:
        if checking_bag in rule[0]:
            current_bag_rule = rule
            break

    # find bags that are in our bag via the rule and sum recursively, adding amount of bags
    #print("Working rule:", current_bag_rule)
    inner_bag_loop_sum = 0
    for inner_bag in current_bag_rule[1]:
        # parse output: (sum, offset_bool)
        output_value = sum_inner_bags_recursively(inner_bag[1])
        sum = output_value[0]
        offset = output_value[1]

        inner_bag_loop_sum += inner_bag[0] * sum
        if offset:
            #print("Add offset of:", inner_bag[0])
            inner_bag_loop_sum += inner_bag[0]

    #print(current_bag_rule[0], "contains", inner_bag_loop_sum, "bags")
    return (int(inner_bag_loop_sum), True)


# example1 = 32
# example2 = 126
f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

# make a list of all the bag rules
bag_rules = []
for rule in infile:
    bag_info = get_bag_info(rule)
    bag_rules.append(bag_info)

# print rules for debug
if 0:
    print("Rules:")
    for rule in bag_rules:
        print(rule)
    print("\n")

start_bag = "shiny gold"
print("End sum:", sum_inner_bags_recursively(start_bag)[0])
