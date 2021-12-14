# parse and read in the navigation
f = open("input1.txt", "r")
navigation = f.read().splitlines()

# loop over each line in the navigation
first_illegal_chars = []
for line in navigation[:]:

    open_chunk_pattern = []  # reset the list per line
    for letter in line:

        # maintain a list of open chars to match against in order
        if letter in ["(", "[", "{", "<"]:
            open_chunk_pattern.append(letter)

        # if it is not an open char it must be a closing char so make sure it matches the latest open char
        else:
            if letter == ")":
                if open_chunk_pattern[-1] != "(":  # if it doesnt match then it is the first illegal char
                    first_illegal_chars.append(letter)  # add it to a list
                    break  # stop reading the line here
            elif letter == "]":
                if open_chunk_pattern[-1] != "[":
                    first_illegal_chars.append(letter)
                    break
            elif letter == "}":
                if open_chunk_pattern[-1] != "{":
                    first_illegal_chars.append(letter)
                    break
            elif letter == ">":
                if open_chunk_pattern[-1] != "<":
                    first_illegal_chars.append(letter)
                    break

            # remove the open chunk part if it is valid (could be incomplete but this is fine for p1)
            open_chunk_pattern.pop(-1)


# answer wants a running sum where each char has a value
sum = 0
for char in first_illegal_chars:  # loop over list of illegal chars and add their value to the sum
    if char == ")":
        sum += 3
    elif char == "]":
        sum += 57
    elif char == "}":
        sum += 1197
    elif char == ">":
        sum += 25137

print("Syntax score:", sum)
