import string
height_map = dict()
for index, letter in enumerate(string.ascii_lowercase):
	height_map[letter] = index + 1
f = open("input", "r")
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
    #print("O", orig, "N", new, "P", path)
    # allow any amount down or strictly 1 above
    if height_map[survey[new]] <= height_map[survey[orig]]+1:
        if new in path:
            #print("Cant go back on oneself")
            return 0
        return 1
    else:
        return 0
    

# function to recursively find the next step in a path
current_path = [s_pos]  # always start at S
g_valid_paths = []
g_shortestLen = 1000000000
g_shortestPath = []
def recurse_step(pos, path_taken):
    global g_valid_paths, g_shortestPath, g_shortestLen

    # stop case if we are still processing a path greater than the current best
    if len(path_taken) > g_shortestLen:
        return

    # GOAL base case reached E
    if pos == e_pos:
        print("FOUND PATH")
        g_shortestPath = path_taken.copy()
        g_shortestLen = len(path_taken)
        return 
        
    # recursive case, take available path
    # UP
    if pos[1] - 1 >= MIN_Y:
        u_pos = (pos[0], pos[1]-1)
        #print("UP pos:", u_pos, "letter:", survey[u_pos])
        if check_valid_path(pos, u_pos, path_taken):
            #print("Up valid")
            new_path = path_taken.copy()
            new_path.append(u_pos)
            #print("NEWPATH:", new_path)
            recurse_step(u_pos, new_path)

    # DOWN
    if pos[1] + 1 <= MAX_Y:
        d_pos = (pos[0], pos[1]+1)
        #print("DOWN pos:", d_pos, "letter:", survey[d_pos])
        if check_valid_path(pos, d_pos, path_taken):
            #print("Down valid")
            new_path = path_taken.copy()
            new_path.append(d_pos)
            #print("NEWPATH:", new_path)
            recurse_step(d_pos, new_path)
    
    # LEFT
    if pos[0] - 1 >= MIN_X:
        l_pos = (pos[0]-1, pos[1])
        #print("LEFT pos:", l_pos, "letter:", survey[l_pos])
        if check_valid_path(pos, l_pos, path_taken):
            #print("Left valid")
            new_path = path_taken.copy()
            new_path.append(l_pos)
            #print("NEWPATH:", new_path)
            recurse_step(l_pos, new_path)
    
    # RIGHT
    if pos[0] + 1 <= MAX_X:
        r_pos = (pos[0]+1, pos[1])
        #print("RIGHT pos:", r_pos, "letter:", survey[r_pos])
        if check_valid_path(pos, r_pos, path_taken):
            #print("Right valid")
            new_path = path_taken.copy()
            new_path.append(r_pos)
            #print("NEWPATH:", new_path)
            recurse_step(r_pos, new_path)
    
    print("BOTTOM NO VALID PATHS. Died at:", len(path_taken), g_shortestLen)

recurse_step(s_pos, current_path)
print()
#print(g_valid_paths)
#print(len(g_valid_paths))

print(g_shortestPath)
print(g_shortestLen-1)