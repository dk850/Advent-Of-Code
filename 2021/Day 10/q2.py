# parse and read in the height map
f = open("input1.txt", "r")
navigation = f.read().splitlines()


# loop over each line in the navigation
completion_strings = []
for line in navigation[:]:

    open_chunk_pattern = []  # reset the list per line
    for pos in range(len(line)):
        letter = line[pos]

        # maintain a list of open chars to match against in order
        if letter in ["(", "[", "{", "<"]:
            open_chunk_pattern.append(letter)

        # if it is not an open char it must be a closing char so make sure it matches the latest open char
        else:
            if letter == ")":
                if open_chunk_pattern[-1] != "(":  # if it doesnt match then it is a corrupt line ignore
                    break
            elif letter == "]":
                if open_chunk_pattern[-1] != "[":
                    break
            elif letter == "}":
                if open_chunk_pattern[-1] != "{":
                    break
            elif letter == ">":
                if open_chunk_pattern[-1] != "<":
                    break

            # remove the open chunk part if it is valid (could be incomplete but this is fine for p1)
            open_chunk_pattern.pop(-1)


        # if we have reached the end of the line we can see what symbols are needed to complete it
        if pos == len(line) - 1:
            if len(open_chunk_pattern) == 0:  # nothing to do
                break

            # else generate a string of closed symbols to match the open symbols
            else:
                closing_string = ""
                for _ in range(len(open_chunk_pattern[:])):  # loop over the current pattern
                    if open_chunk_pattern[-1] == "(":  # match the symbol
                        closing_string += ")"  # add it to the string
                    elif open_chunk_pattern[-1] == "[":
                        closing_string += "]"
                    elif open_chunk_pattern[-1] == "{":
                        closing_string += "}"
                    elif open_chunk_pattern[-1] == "<":
                        closing_string += ">"

                    open_chunk_pattern.pop(-1)  # then pop the value

                # append string to the list
                completion_strings.append(closing_string)



# determine the score of each string
scores = []
for c_string in completion_strings:
    score = 0

    # apply rules to each letter in the string
    for char in c_string:
        score *= 5

        if char == ")":
            score += 1
        elif char == "]":
            score += 2
        elif char == "}":
            score += 3
        elif char == ">":
            score += 4
    scores.append(score)


# answer wants us to find the middle score from the autocompleters
scores.sort()
print("Median score:", scores[int((len(scores)-1)/2)])  # get median
