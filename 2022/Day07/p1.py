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
                
                # else it is a file to calculate size of
                else:
                    size += int(input[inspos][0])
            d_sizes["".join([str(x) for x in d_stack])] = size
            
    inspos+=1
    if inspos == len(input):
        break

#print()
#print("BASE_SIZES", d_sizes)


# sort the array of children assignment by number of children so we can fill it depth first
s_d_kids={}
for k in sorted(d_kids, key=lambda k: len(d_kids[k]), reverse=False):
    s_d_kids[k]=d_kids[k]
#print("KID_ASSIGN", s_d_kids)
#print()

while True:
    #print()
    #print("WHILE")

    p_key_to_remove = []
    for p_key in s_d_kids:
        # check the values (inner kids) aren't dependant on a different (parent) key
        #print("parent", p_key)

        for k_key in s_d_kids[p_key]:
            #print("kid", k_key)
            if k_key in s_d_kids.keys():
                #print("DEPENDANT", k_key)
                break
        
        # if k_keys not depenant, apply to sizes and remove p_key from s_d_keys
        else:  # will only enter here if break above is not called
            #print("apply to", d_sizes[p_key])

            for k_key in s_d_kids[p_key]:
                #print("add", d_sizes[k_key])
                d_sizes[p_key] += d_sizes[k_key]
            p_key_to_remove.append(p_key)

    # remove keys and continue loop if any remain in s_d_kids
    #print("start", s_d_kids)
    for remove in p_key_to_remove:
        del s_d_kids[remove]
    #print("end", s_d_kids)
    if len(s_d_kids) == 0:
        break
#print(s_d_kids, d_sizes)

# final loop to get answer
sum=0
for key in d_sizes:
    if d_sizes[key] <= 100000:
        sum += d_sizes[key]
print(sum)