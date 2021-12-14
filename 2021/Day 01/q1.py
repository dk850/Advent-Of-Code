# Read file into a list
f = open("input1.txt", "r")
mylist = f.read().splitlines()

# setup variables
depth_increase_count = 0
previous_value = mylist[0]  # first value in list at index 0


for value in mylist:  # loop over each value in the list
    if int(value) > int(previous_value):  # make sure btoh are integers, then if the current is bigger than the previous
        depth_increase_count += 1  # add 1 to the increase
    previous_value = value  # the current value now needs to become the previous value for the next iteration

print(depth_increase_count)  # print
