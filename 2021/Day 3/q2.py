f = open("input1.txt", "r")
mylist = f.read().splitlines()

t_mylist = list(zip(*mylist))  # transpose the list
# column 1 is now the first element in this list


# loop over the elements in the transposed list to build the binary strings of the gamma and epsilon values
gamma_string = ''
epsilon_string = ''
for element in t_mylist:
    zeros = element.count('0')  # count 0s in the string
    ones  = element.count('1')  # count 1s

    # build strings
    gamma_string += '1' if ones > zeros else '0'  # most common bit per list
    epsilon_string += '0' if ones > zeros else '1'  # least common bit per list


# convert binary strings to int
gamma_int = int(gamma_string, 2)
epsilon_int = int(epsilon_string, 2)

# print multiply for answer
print(gamma_int * epsilon_int)
