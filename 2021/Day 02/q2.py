f = open("input1.txt", "r")
mylist = f.read().splitlines()

position = [0, 0, 0]  # our position as horizontal, depth and aim

# Decode instructions
for item in mylist:
    instruction = item.split(' ')  # instructions consist of WORD_SPACE_NUMBER, so split on the space
    command = instruction[0]  # the WORD part
    value = int(instruction[1])  # the number part as an integer


    # decode the command
    if command == "forward":  # modify our horizontal position
        position[0] += value  # increase horizontal
        position[1] += position[2]*value  # increase depth by aim multiplied by value

    elif command == "down":  # modify our depth
        #position[1] += value  # increase depth
        position[2] += value  # increase aim

    elif command == "up":  # modify our depth
        #position[1] -= value  # decrease depth
        position[2] -= value  # decrease aim

    else:
        print("unrecognised command: "+command)  # make sure we account for all commands



print(position)
print(position[0]*position[1])  # answer wants us to multiply these together
