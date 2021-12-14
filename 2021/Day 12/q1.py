# parse and read in the list of possible navigations
f = open("../worklist.txt", "r")
path_rules = [x.split('-') for x in f.read().splitlines()]

print(path_rules)
