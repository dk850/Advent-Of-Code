def check_list(list, goal_number):
    # innefficient but works fine for our numbers
    for i in list:
        for j in list:
            if i + j == goal_number:
                return True
    return False

def find_sum(input_list, goal_number):
    valid = False

    for main_position in range(len(input_list)):
        running_sum = input_list[main_position]
        added_numbers_list = [running_sum]

        #print("Starting sum:", running_sum, "Goal:", goal_number)
        for extra_index in range(main_position, len(input_list)):

            # add next n contiguous values in list until we reach goal value (pass) or get a greater value (fail)
            try:
                #print("Adding:", input_list[extra_index+1])
                running_sum += input_list[extra_index+1]
                added_numbers_list.append(input_list[extra_index+1]) # also add it to list of valid numbers set
                #print("New sum:", running_sum)

                # if at any point we find goal number we have a winner
                if running_sum == goal_number:
                    valid = True
                    break

                # if sum becomes bigger than goal we cant make it smaller so failed, start on next main_position
                elif running_sum > goal_number:
                    break

            # wrap in a try in case we try to add past the end of the list (IndexError)
            except IndexError:
                pass

            # if we encounter an unknown error we need to print it for debug
            except:
                print(sys.exc_info()[0])

        if(valid):
            #print("found valid set:", added_numbers_list)
            return added_numbers_list

    # shouldnt be able to get here with valid input
    return -1

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

# check if any pairs in previous list sum to the goal (next number in overall list)
for i in range(preamble_size, len(infile)):
    goal_number = int(infile[i])
    #print("List:", previous_numbers_list)
    #print("Goal:", goal_number)

    # check if the sum of 2 numbers make the goal number
    if check_list(previous_numbers_list, goal_number):

        # change list & goal for next iteration
        previous_numbers_list.append(goal_number)
        del previous_numbers_list[0]
        goal_number = infile[i]

    # we have found the number that breaks the pattern
    else:
        #print("Failed property check:", goal_number)
        break

# make list elements ints before starting calculations
XMAS_list = []
for item in infile:
    XMAS_list.append(int(item))

# find contiguous set in list that sum to goal number
valid_set = find_sum(XMAS_list, goal_number)

# sort it and add biggest to smallest for final answer
valid_set.sort()
print("Valid list sorted:", valid_set)
print("Answer:", valid_set[0] + valid_set[-1])
