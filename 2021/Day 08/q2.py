def string_to_set(string):  # turns a string into a set and returns the set
    rv = set()
    for letter in string:
        rv.add(letter)
    return rv

def set_to_string(set):  # turns a set into a string and returns the string
    rv = ""
    for item in set:
        rv += item
    return rv


# parse and read in the notes and the output
f = open("input1.txt", "r")
note_lines = f.read().splitlines()
note_lines = [x.split(' | ') for x in note_lines]  # split delimiter
note_lines = [[note.split(' '), output.split(' ')] for (note, output) in note_lines]  # split on spaces


# part 2 wants us to decode the output based on 10 inputs so;
#    need to decode which unique mix of letters in a random order are which letter
running_total = 0  # the answer wants us to add up all the output numbers
for recorded_signal in note_lines:

    # assign variables
    recorded_signal_values = recorded_signal[0]
    output_signal = recorded_signal[1]

    # initialise dictionary as it is different for each recorded line
    segment_letters = {}

    ## DECODE
    # go over each number in the recorded signal and get the unique letters to determine the segments.
    while 1:
        for number in recorded_signal_values:
            # 1
            if (len(number) == 2) and ("1" not in segment_letters.keys()):
                #print("Decoded 1:", number)
                segment_letters["1"] = set(number[0])
                segment_letters["1"].add(number[1])
            # 4
            elif (len(number) == 4) and ("4" not in segment_letters.keys()):  # number 4
                #print("Decoded 4:", number)
                segment_letters["4"] = set(number[0])
                segment_letters["4"].add(number[1])
                segment_letters["4"].add(number[2])
                segment_letters["4"].add(number[3])
            # 7
            elif (len(number) == 3) and ("7" not in segment_letters.keys()):  # number 7
                #print("Decoded 7:", number)
                segment_letters["7"] = set(number[0])
                segment_letters["7"].add(number[1])
                segment_letters["7"].add(number[2])
            # 8
            elif (len(number) == 7) and ("8" not in segment_letters.keys()):  # number 8
                #print("Decoded 8:", number)
                segment_letters["8"] = set(number[0])
                segment_letters["8"].add(number[1])
                segment_letters["8"].add(number[2])
                segment_letters["8"].add(number[3])
                segment_letters["8"].add(number[4])
                segment_letters["8"].add(number[5])
                segment_letters["8"].add(number[6])


            # for each loop we should be able to decode a further value based on set rules
            # length 6 numbers: 0, 6, 9
            elif (len(number) == 6) and (("0" not in segment_letters.keys()) or \
                    ("6" not in segment_letters.keys()) or ("9" not in segment_letters.keys())):
                # 9
                if ("4" in segment_letters.keys()) and ("7" in segment_letters.keys()) and ("9" not in segment_letters.keys()):
                    union_set = segment_letters["4"].union(segment_letters["7"])  # the union of 4 and 7 leaves LL and B empty
                    if len(string_to_set(number).difference(union_set)) == 1:  # if theres 1 missing value from the difference we have found 9
                        #print("Decoded 9:", number)
                        segment_letters["9"] = set(number[0])
                        segment_letters["9"].add(number[1])
                        segment_letters["9"].add(number[2])
                        segment_letters["9"].add(number[3])
                        segment_letters["9"].add(number[4])
                        segment_letters["9"].add(number[5])
                # 0
                if ("9" in segment_letters.keys()) and ("1" in segment_letters.keys()) and \
                        (len(string_to_set(number).difference(segment_letters["1"])) == 4) and \
                        ("0" not in segment_letters.keys()):  # 0-1 would leave 4 letters whereas 6-1 would leave 5
                    if string_to_set(number) == segment_letters["9"]:  # 9-1 would also leave 4 so we get this first above and check we arent looking at the same number here
                        continue
                    #print("Decoded 0:", number)
                    segment_letters["0"] = set(number[0])
                    segment_letters["0"].add(number[1])
                    segment_letters["0"].add(number[2])
                    segment_letters["0"].add(number[3])
                    segment_letters["0"].add(number[4])
                    segment_letters["0"].add(number[5])
                # 6
                if ("9" in segment_letters.keys()) and ("1" in segment_letters.keys()) and \
                        (len(string_to_set(number).difference(segment_letters["1"])) == 5) and \
                        ("6" not in segment_letters.keys()):  # 0-1 would leave 4 letters whereas 6-1 would leave 5
                    if string_to_set(number) == segment_letters["9"]:
                        continue
                    #print("Decoded 6:", number)
                    segment_letters["6"] = set(number[0])
                    segment_letters["6"].add(number[1])
                    segment_letters["6"].add(number[2])
                    segment_letters["6"].add(number[3])
                    segment_letters["6"].add(number[4])
                    segment_letters["6"].add(number[5])

            # numbers 2, 3 and 5
            elif (len(number) == 5) and (("2" not in segment_letters.keys()) or \
                    ("3" not in segment_letters.keys()) or ("5" not in segment_letters.keys())):
                # 3
                if ("1" in segment_letters.keys()) and ("3" not in segment_letters.keys()) and \
                        (len(string_to_set(number).difference(segment_letters["1"])) == 3):  # 3-1 is 3 long, whereas 2-1 and 5-1 are both 4
                    #print("Decoded 3:", number)
                    segment_letters["3"] = set(number[0])
                    segment_letters["3"].add(number[1])
                    segment_letters["3"].add(number[2])
                    segment_letters["3"].add(number[3])
                    segment_letters["3"].add(number[4])
                # 2, 5
                if ("6" in segment_letters.keys()) and ("3" in segment_letters.keys()):  # we can use the number 6 to decode 2 and 5 if we have 3
                    # 2
                    if (len(string_to_set(number).difference(segment_letters["6"])) == 1) and ("2" not in segment_letters.keys()):  # 6-2 leaves 1
                        if string_to_set(number) == segment_letters["3"]:  # make sure we arent looking at 3
                            continue
                        #print("Decoded 2:", number)
                        segment_letters["2"] = set(number[0])
                        segment_letters["2"].add(number[1])
                        segment_letters["2"].add(number[2])
                        segment_letters["2"].add(number[3])
                        segment_letters["2"].add(number[4])
                    # 5
                    if (len(string_to_set(number).difference(segment_letters["6"])) == 0) and ("5" not in segment_letters.keys()):  # 6-5 leaves 0
                        if string_to_set(number) == segment_letters["3"]:  # make sure we arent looking at the number 3
                            continue
                        #print("Decoded 5:", number)
                        segment_letters["5"] = set(number[0])
                        segment_letters["5"].add(number[1])
                        segment_letters["5"].add(number[2])
                        segment_letters["5"].add(number[3])
                        segment_letters["5"].add(number[4])

        if len(segment_letters) == 10:  # end while loop when we have all numbers
            break


    ## GET OUTPUT
    # decode the entries as strings to make it easy to do
    output_amount = ""
    for number in output_signal:

        # skip decoding easy (unique) numbers
        if len(number) == 2:
            #print("Found 1:", number)
            output_amount += "1"
        elif len(number) == 4:
            #print("Found 4:", number)
            output_amount += "4"
        elif len(number) == 3:
            #print("Found 3:", number)
            output_amount += "7"
        elif len(number) == 7:
            #print("Found 8:", number)
            output_amount += "8"

        # else we need to decode using positions from the above dictionary
        else:
            if len(number) == 5:  # it could be 2, 3, 5
                if string_to_set(number) == segment_letters["2"]:
                    #print("Found 2:", number)
                    output_amount += "2"
                elif string_to_set(number) == segment_letters["3"]:
                    #print("Found 3:", number)
                    output_amount += "3"
                elif string_to_set(number) == segment_letters["5"]:
                    #print("Found 5:", number)
                    output_amount += "5"
            else:  # else must be length 6 - could be  0, 6, 9
                if string_to_set(number) == segment_letters["0"]:
                    #print("Found 0:", number)
                    output_amount += "0"
                elif string_to_set(number) == segment_letters["6"]:
                    #print("Found 6:", number)
                    output_amount += "6"
                elif string_to_set(number) == segment_letters["9"]:
                    #print("Found 9:", number)
                    output_amount += "9"

    #print(output_amount)
    running_total += int(output_amount)
    
print("Total:", running_total)
