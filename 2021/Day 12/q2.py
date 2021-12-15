from collections import Counter


# recursively visit neighbours
def r_neighbour_visit(node, visited):
    paths = []  # list to hold valid paths

    # base case we have reached the end, else add the node to the visited list
    if node == "end":
        visited += ","+node
        return [visited]  # return visted nodes as a list
    elif node == "start":
        visited += node
    else:
        visited += ","+node  # add current node to visited string with comma

    # loop over all the neighbours of the current node
    for nbr in node_neighbours[node]:
        if nbr == "start":
            continue  # skip - can only leave start cave once

        # if there are 2 occurances of any small cave, we can no longer double
        if nbr.islower() and (nbr in visited):

            # count frequency of each element that is lower case, splitting the string on commas. if this is 2 then we cant explore more small caves > 1 time
            if 2 in [freq for freq in Counter([x for x in visited.split(',') if x.islower()]).values()]:
                continue  # skip further processing this run


        paths.extend(r_neighbour_visit(nbr, visited))  # else recursively go down each path
        # we use extend here to add lists to a list as individual elements

    return paths  # return the list



# parse and read in the list of possible navigations
f = open("input1.txt", "r")
path_rules = [x.split('-') for x in f.read().splitlines()]


# get unique nodes from the ruleset into a dictionary as keys with the value as their neighbours
node_neighbours = {}
for rule in path_rules:
    # make sure the keys exist
    if rule[0] not in node_neighbours.keys():
        node_neighbours[rule[0]] = []
    if rule[1] not in node_neighbours.keys():
        node_neighbours[rule[1]] = []

    # build the map
    node_neighbours[rule[0]].append(rule[1])
    node_neighbours[rule[1]].append(rule[0])


# recursively look for and return a list of valid paths for all different small caves
print("Processing...")
paths = r_neighbour_visit("start", "")
print("Path count:", len(paths))
