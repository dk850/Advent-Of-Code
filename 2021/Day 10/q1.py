# parse and read in the height map
f = open("input1.txt", "r")
input_heightmap = f.read().splitlines()
heightmap = [list(int(x) for x in x) for x in input_heightmap]  # separate each string into its own int element in the list
