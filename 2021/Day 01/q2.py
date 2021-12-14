f = open("input1.txt", "r")
mylist = f.read().splitlines()
mylist = [int(line) for line in mylist]  # convert to integers
print(mylist)

depth_increase_count = 0
previous_window = mylist[0] + mylist[1] + mylist[2]  # first window is first 3 values
for pos in range(len(mylist)):
    if pos + 2 == len(mylist):  # if calculating another window will look outside the range of the list, stop
        break

    window = mylist[pos] + mylist[pos+1] + mylist[pos+2]  # calculate next window
    if window > previous_window:  # check if it is bigger
        depth_increase_count += 1

    previous_window = window  # reset for next iteration


print(depth_increase_count)
