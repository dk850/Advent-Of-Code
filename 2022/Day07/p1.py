import operator
f = open("input", "r")
input = f.read().splitlines()
input = [x.split(' ') for x in input ]  # split input on , to separate it easier

dir_stack=[]  # where we are
cd_seen_dirs=[]  # list of already seen dir names. Can have duplicates so must rename
dir_seen_dirs=[]  # list of already seen dir names. Can have duplicates so must rename
dir_sizes={}  # monitor size of directories
dir_id=0

for line in input:
    #print(line)

    # check for command pattern
    if line[0] == '$':
        if line[1] == "cd":  # control the directory stack
            if line[2] == "..":  # pop directory
                dir_stack.pop()
            else:
                #dir_name="".join([str(x) for x in dir_stack])+str(line[2])
                if line[2] == "/":
                    dir_name=str(line[2])
                else:
                    dir_name=str(dir_stack[-1])+str(line[2])
                print("DIRNAME", dir_name)
                dir_stack.append(dir_name)

    else:  # else we are looking at the 'ls' output
        if line[0] == "dir":  # if nested dir, process later
            print("STAK:", dir_stack, line[1])
            child_dir_name=str(dir_stack[-1])+str(line[1])
            print("CDIRNAME", child_dir_name)

            if dir_stack[-1] in dir_sizes.keys():
                dir_sizes[dir_stack[-1]][1].append(child_dir_name)
            else:
                dir_sizes[dir_stack[-1]] = [int(0), [child_dir_name]]
            print(dir_sizes)

        else:  # calculate sum of files for given dir
            if dir_stack[-1] in dir_sizes.keys():
                dir_sizes[dir_stack[-1]][0] += int(line[0])
            else:
                dir_sizes[dir_stack[-1]] = [int(line[0]), []]

print("Current stack:")
print(dir_sizes)
print()

dir_kids={}
for key in dir_sizes.keys():
    dir_kids[key] = len(dir_sizes[key][1])
    print(key, dir_sizes[key], len(dir_sizes[key][1]))
dir_kids = dict( sorted(dir_kids.items(), key=operator.itemgetter(1)))  # reverse sort the dict


for dir in dir_kids:
    if dir_kids[dir] == 0:
        continue
    print("Working on", dir)

    outsize=0
    for child in dir_sizes[dir][1]:
        print("Adding child size", child, dir_sizes[child][0])
        outsize += dir_sizes[child][0]
    print("outside:", outsize)
    dir_sizes[dir][0] += outsize
    print()


print("End stack:")
print(dir_sizes)

outsum=0
for item in dir_sizes:
    if dir_sizes[item][0] < 100000:
        outsum+=dir_sizes[item][0]
print("Final sum of dirs with size <= 100000:", outsum)
