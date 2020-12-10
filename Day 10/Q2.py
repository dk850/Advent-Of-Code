def find_difference(num1, num2):
    #print(num1, num2, "difference", num2-num1)
    return num2-num1

def is_mapping_valid(check_list):
    # use dictionary to store joltage numbers, return validity of mapping
    differences = {1:0, 2:0, 3:0}

    for i in range(len(check_list)):
        if (i + 1) == len(check_list):
            break
        try:
            difference = find_difference(check_list[i], check_list[i+1])
            differences[difference] += 1
        except KeyError:
            return False
        except:
            print(sys.exc_info()[0])

    #print("Valid dictionary:", differences)
    return True

def find_permutations(input_list):
    # if list is too small to change anything there is only 1 permutation
    if len(input_list) < 3:
        return 1

    #print("Checking list:", input_list)
    working_list = input_list.copy()
    changeable_list = input_list.copy()
    del changeable_list[0]
    del changeable_list[-1]
    #print("Changeable Numbers:", changeable_list)

    # if we can remove the only element then it is 2 permutations
    if len(changeable_list) == 1:
        working_list.remove(changeable_list[0])
        if is_mapping_valid(working_list):
            return 2
        else:
            return 1

    # if there are only 2 changeable elements and both can be removed at the same time, that is 4 permutations
    elif len(changeable_list) == 2:
        del working_list[1]
        del working_list[1]
        if is_mapping_valid(working_list):
            return 4
        else:
            print("invalid?") # shouldnt get here

    permutation_count = 0
    for i in range(len(changeable_list)):
        working_list.remove(changeable_list[i])

        if is_mapping_valid(working_list):
            permutation_count += 1
        else:
            print("invalid?") # shouldnt get here

        working_list.insert(i+1, changeable_list[i])

    # since there are no 2 gaps, each 3 changeable list is 7 if valid for each removal
    if permutation_count == len(changeable_list):
        if permutation_count == 3:
            return 7
        else:
            print("invalid?") # shouldnt get here
    else:
        print("invalid?") # shouldnt get here

    return 1 # shouldnt get here


f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

# build array
sorted_array = []
for item in infile:
    sorted_array.append(int(item))
sorted_array.sort()
#print("Values:", sorted_array)

# if the gap is 3, both numbers MUST be present, split the list here
main_array = []
temp_array = [0]    # always start at 0 in the first list
for i in range(len(sorted_array)):
    temp_array.append(sorted_array[i])

    if (i + 1) == len(sorted_array): # finished
        #print("Adding:", temp_array)
        main_array.append(temp_array.copy())
        main_array.append([main_array[-1][-1] + 3]) # add max value onto list
        break

    elif find_difference(sorted_array[i], sorted_array[i+1]) == 3:
        main_array.append(temp_array.copy())
        temp_array.clear()

print("Main Array:", main_array)

answer = 1
for sub_list in main_array:
    answer *= find_permutations(sub_list)
print(answer)
