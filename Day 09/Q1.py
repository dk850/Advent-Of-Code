def check_list(list, goal_number):
    for i in list:
        for j in list:
            if i + j == goal_number:
                return True
    return False

f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

# for debug
if 0:
    print("Data:")
    for line in infile:
        print(line)
    print("\n")

# build initial preamble list
preamble_size = 25
previous_numbers_list = []
for i in range(preamble_size):
    previous_numbers_list.append(int(infile[i]))

# check each number in list is a sum of previous preamble_size
for i in range(preamble_size, len(infile)):
    goal_number = int(infile[i])
    #print("List:", previous_numbers_list)
    #print("Goal:", goal_number)

    # check if the sum of 2 numbers make the goal number
    if check_list(previous_numbers_list, goal_number):

        # change list for next iteration if number is valid
        previous_numbers_list.append(goal_number)
        del previous_numbers_list[0]
        goal_number = infile[i]

    else:
        print("Failed property check:", goal_number)
        break

# could improve the check list function to sort the list and add top to tail
# and decrease either top or tail if too big or too small compared to goal number
