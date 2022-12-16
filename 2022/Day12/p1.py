from importlib.resources import path
import string
height_map = dict()
for index, letter in enumerate(string.ascii_lowercase):
	height_map[letter] = index + 1
f = open("example", "r")
input = f.read().splitlines()

# Function to print the map (survey or directional)
def print_map(map_type):
    for y in range(max(map_type.keys())[1]):
        println=""
        for x in range(max(map_type.keys())[0]):
            println += map_type[(x, y)]
        print(println)

# assign coordinates to each letter
survey = {}
x = 0
y = 0
for line in input:
    for letter in line:
        survey[(x, y)] = letter
        x += 1
    x = 0
    y += 1

# Show starter map
print_map(survey)

# get S and E pos. Turn into real elevations
s_pos=list(survey.keys())[list(survey.values()).index("S")]
e_pos=list(survey.keys())[list(survey.values()).index("E")]
survey[s_pos] = "a"  # Set S to be its actual elevation, a
survey[e_pos] = "z"  # set E to be its actual elevation, z

# parse borders for readability
MIN_X = 0
MIN_Y = 0
MAX_X = max(list(x[0] for x in survey.keys()))
MAX_Y = max(list(y[1] for y in survey.keys()))

# print for debug 
print("S:", s_pos)
print("E:", e_pos)
print()

# helper function to compare elevations - 1/True yes_move || 0/False no_move
def check_valid_path(orig, new, path):
    print("O", orig, "N", new, "P", path)
    # allow any amount down or strictly 1 above
    if height_map[survey[new]] <= height_map[survey[orig]]+1:
        if path[-1] == new:
            #print("Cant go back on oneself")
            return 0
        return 1
    else:
        return 0
    

# function to recursively find the next step in a path
g_valid_paths = []
def recurse_step(pos, path_taken):
    global g_valid_paths
    print(path_taken)
    move = True  # can only move one time per recurse
    
    # GOAL base case reached E
    if pos == e_pos:
        g_valid_paths.append(path_taken)
        move = False
    
    #print("Current pos:", pos, "letter:", survey[pos], "height map:", height_map[survey[pos]])
        
    # recursive case, take available path
    # UP
    if pos[1] - 1 >= MIN_Y and move:
        u_pos = (pos[0], pos[1]-1)
        ##print("UP pos:", u_pos, "letter:", survey[u_pos])
        if check_valid_path(pos, u_pos, path_taken):
            print("Up valid")
            recurse_step(u_pos, path_taken+str(", "+u_pos))
            print("HERE", path_taken)

    # DOWN
    if pos[1] + 1 <= MAX_Y and move:
        d_pos = (pos[0], pos[1]+1)
        ##print("DOWN pos:", d_pos, "letter:", survey[d_pos])
        if check_valid_path(pos, d_pos, path_taken):
            print("Down valid")
            recurse_step(d_pos, path_taken+d_pos)
    
    # LEFT
    if pos[0] - 1 >= MIN_X and move:
        l_pos = (pos[0]-1, pos[1])
        ##print("LEFT pos:", l_pos, "letter:", survey[l_pos])
        if check_valid_path(pos, l_pos, path_taken):
            print("Left valid")
            recurse_step(l_pos, path_taken+l_pos)
    
    # RIGHT
    if pos[0] + 1 <= MAX_X and move:
        r_pos = (pos[0]+1, pos[1])
        ##print("RIGHT pos:", r_pos, "letter:", survey[r_pos])
        if check_valid_path(pos, r_pos, path_taken):
            print("Right valid")
            recurse_step(r_pos, path_taken+r_pos)

recurse_step(s_pos, "")
print()
print(len(g_valid_paths))