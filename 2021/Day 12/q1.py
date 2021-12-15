# recursively visit neighbours
def r_neighbour_visit(node, visited):
    paths = []  # list to hold valid paths

    # base case we have reached the end
    if node == "end":
        visited += node
        return [visited]  # return visted nodes as a list
    else:
        visited += node+","  # add current node to visited string with comma

    for nbr in node_neighbours[node]:
        if nbr.islower() and (nbr in visited):  # cant re-vist small caves
            continue
        else:
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


# recursively look for and return a list of valid paths
paths = r_neighbour_visit("start", "")
print("Path count:", len(paths))
