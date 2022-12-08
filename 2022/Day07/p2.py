f = open("input", "r")
input = f.read().splitlines()
input = [x.split(' ') for x in input ]  # split input on , to separate it easier

d_stack=[]
d_sizes={}
d_kids={}

# Generate unique dictionarys of base size and assignment
inspos = 0
while True:
    #print(input[inspos])

    # decode instruction
    if "$" in input[inspos]:
        if input[inspos][1] == "cd":
            # pop directory from stack
            if input[inspos][2] == "..":
                d_stack.pop()

            # add directory to stack
            else:
                d_stack.append(input[inspos][2])


        # calculate child dirs and size of this dir
        elif input[inspos][1] == "ls":
            size = 0
            while True:
                inspos+=1  # increase count
                
                # if end of file
                if inspos == len(input)-1:
                    size += int(input[inspos][0])
                    break

                # if dir, add as child
                elif input[inspos][0] == "dir": 
                    prefix="".join([str(x) for x in d_stack])  # generate prefix string
                    if prefix not in d_kids.keys():  # create entry if missing
                        d_kids[prefix] = []
                    d_kids[prefix].append(str(prefix+input[inspos][1]))  # add child assignment to prefix

                # if command pattern, stop
                elif input[inspos][0] == "$":
                    inspos-=1  # count back one
                    break
                
                # else add to the child size
                else:
                    size += int(input[inspos][0])
            d_sizes["".join([str(x) for x in d_stack])] = size
            
    inspos+=1
    if inspos == len(input):  # break loop if we reach end of instructions
        break
#print()
#print("BASE_SIZES", d_sizes)


# sort the array of children assignment by number of children so we can fill it depth first
s_d_kids={}
for k in sorted(d_kids, key=lambda k: len(d_kids[k]), reverse=False):
    s_d_kids[k]=d_kids[k]
#print("KID_ASSIGN", s_d_kids)
#print()

# loop until no kids to assign 
while True:
    #print()
    #print("WHILE")

    p_key_to_remove = []  # cant dynamically edit list whilst looping on it
    for p_key in s_d_kids:
        #print("parent", p_key)

        # check the values (inner kids) aren't dependant on a different (parent) key
        for k_key in s_d_kids[p_key]:
            #print("kid", k_key)
            if k_key in s_d_kids.keys():
                #print("DEPENDANT", k_key)
                break
        
        # if k_keys not depenant, apply to sizes and remove p_key from s_d_keys
        else:  # will only enter here if loop above is exhausted and not broken
            #print("apply to", d_sizes[p_key])

            for k_key in s_d_kids[p_key]:
                #print("add", d_sizes[k_key])
                d_sizes[p_key] += d_sizes[k_key]
            p_key_to_remove.append(p_key)

    # remove keys from main kid dict
    for remove in p_key_to_remove:
        del s_d_kids[remove]

    if len(s_d_kids) == 0:  # exit while if no kids left 
        break


# final loop to get answer
sum=0
for key in d_sizes:
    if d_sizes[key] <= 100000:
        sum += d_sizes[key]
#print(sum)


### P2
# calculate how much space we must free
print("Total used size:", d_sizes["/"])
unused_space = 70000000-d_sizes["/"]
print("Unused space currently:", unused_space)
to_free = 30000000-unused_space
print("Must free up:", to_free)

# get directory to delete
candidate = ""
can_size = 1111111111111111111111
for dir in d_sizes.keys():
    
    # if size of dir is big enough to free enough space, store it
    if d_sizes[dir] >= to_free:
        print("CANDIDATE")
        
        # check if we have a smaller candidate than currently
        if d_sizes[dir] < can_size:
            print("smaller") 
            candidate = dir  # if not, update the dir we will delete
            can_size = d_sizes[dir]

print("OUT:", can_size)  # dir to delete, answer
