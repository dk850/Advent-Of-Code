f = open("example", "r")
input = f.read().splitlines()
#input = [x.split(',') for x in input ]  # split input on , to separate it easier

dir_stack=[]  # where we are
dir_sizes={}  # monitor size of directories
dir_size=0

for line in input:
    line = line.split(' ')
    #print(line)

    # check for command pattern
    if line[0] == '$':
        if line[1] == "cd":  # dont need to do anything on 'ls'
            if line[2] == "..":  # pop directory
                dir_stack.pop()
            else:
                dir_stack.append(line[2])

    else:  # else we are looking at the 'ls' output
        if line[0] == "dir":  # if nested dir, process later
            if dir_stack[-1] in dir_sizes.keys():
                dir_sizes[dir_stack[-1]][1].append(line[1])
            else:
                dir_sizes[dir_stack[-1]] = [int(0), [line[1]]]

        else:  # calculate sum of files for given dir
            if dir_stack[-1] in dir_sizes.keys():
                dir_sizes[dir_stack[-1]][0] += int(line[0])
            else:
                dir_sizes[dir_stack[-1]] = [int(line[0]), []]

print("Current stack:")
print(dir_sizes)





exit()

# process nested directories
def depth_first(parent, nest):
    print()
    print("Processing:", nest, "From:", parent)
    for dir in nest:
        print("Recursing:", dir, dir_sizes[dir][1])

        # Base case no nested dirs, add size to given dir, remove the nest from parent
        if len(dir_sizes[dir][1]) == 0:
            dir_sizes[parent][1].remove(dir)
            return dir_sizes[dir][0]
        else:
            rval=depth_first(dir, dir_sizes[dir][1])
            print("Got returned", dir, "value", rval, "+", dir_sizes[dir][0], "=", dir_sizes[dir][0] + rval)
            dir_sizes[dir][0] += rval


    print("End")

depth_first("/", dir_sizes['/'][1])  # loop over nested dirs from /
print("End stack:")
print(dir_sizes)






exit()




base_dir_keys=[]
while True:
    for dir in dir_sizes:
        print("Processing:", dir)
        print(dir_sizes[dir])

        if type(dir_sizes[dir]) is int:  # dont need to process base dirs
            base_dir_keys.append(dir)
            continue

        if dir_sizes[dir][1] != []:
            to_remove=[]
            for nested_dir in dir_sizes[dir][1]:
                if nested_dir in base_dir_keys:
                    dir_sizes[dir][0] += dir_sizes[nested_dir]
                    to_remove.append(nested_dir)
            for removal in to_remove:
                dir_sizes[dir][1].remove(removal)

        else:
            dir_sizes[dir] = dir_sizes[dir][0]  # translate to bare int

    if len(base_dir_keys) == len(dir_sizes.keys()):
        break
print(dir_sizes)
