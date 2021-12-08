# parse and read in the notes and the output
f = open("testlist.txt", "r")
note_lines = f.read().splitlines()
note_lines = [x.split(' | ') for x in note_lines]  # split delimiter
note_lines = [[note.split(' '), output.split(' ')] for (note, output) in note_lines]  # split on spaces

# part 2 wants us to decode the output based on 10 inputs so;
#    need to decode which line on the display corresponds to which letter

# DICTIONARY KEY
# T  = Top
# UL = Upper Left
# UR = Upper Right
# M  = Middle
# LL = Lower Left
# LR = Lower Right
# B  = Bottom

running_total = 0  # the answer wants us to add up all the output numbers
for recorded_signal in note_lines:
    print()
    print("NEW SIGNAL")
    # assign variables
    recorded_signal_values = recorded_signal[0]
    output_signal = recorded_signal[1]

    # initialise dictionary as it is different for each recorded line
    segment_positions = {}  # store our positions in a dictionary for easy assigning
    segment_positions["T"]  = set()  #         T T T
    segment_positions["UL"] = set()  #       UL     UR
    segment_positions["UR"] = set()  #       UL     UR
    segment_positions["M"]  = set()  #         M M M
    segment_positions["LL"] = set()  #       LL     LR
    segment_positions["LR"] = set()  #       LL     LR
    segment_positions["B"]  = set()  #         B B B


    # go over each number in the recorded signal and decode the inputs to determine the segment lines
    for number in recorded_signal_values:
        print(number)
        if len(number) == 2:    # number 1
            print("Decoded 1")
            segment_positions["UR"].add(number[0])
            segment_positions["UR"].add(number[1])
            segment_positions["LR"].add(number[0])
            segment_positions["LR"].add(number[1])

        elif len(number) == 4:  # number 4
            print("Decoded 4")
            segment_positions["UL"].add(number[0])
            segment_positions["UR"].add(number[1])
            segment_positions["M"].add(number[2])
            segment_positions["LR"].add(number[3])

        elif len(number) == 3:  # number 7
            print("Decoded 7")
            segment_positions["T"].add(number[0])
            segment_positions["UR"].add(number[1])
            segment_positions["LR"].add(number[2])

        #elif len(number) == 7:  # number 8
        #    print("Decoded 8")
        #    segment_positions["T"].add(number[0])
        #    segment_positions["UL"].add(number[1])
        #    segment_positions["UR"].add(number[2])
        #    segment_positions["M"].add(number[3])
        #    segment_positions["LL"].add(number[4])
        #    segment_positions["LR"].add(number[5])
        #    segment_positions["B"].add(number[6])
        else:
            continue
        print(segment_positions)

    # reduce list to correct letters only
    single_set = set()
    while 1:
        done_count = 0  # counter to see how many positions are complete so we can break out the while loop

        # loop over all positions until each only has 1 letter
        for position in segment_positions:

            # if theres only 1 element for the dictionary empty, this must be correct, so remove it everywhere else
            if len(segment_positions[position]) == 1:
                print("length1", position)
                done_count += 1
                single_set.add(segment_positions[position][0])  # add this position to a set (no duplicates in a set)

            # if the entry has more than 1 letter, we can remove those that are already specified elsewhere
            if len(segment_positions[position]) != 1:
                for letter in single_set:
                    while letter in segment_positions[position]: segment_positions[position].remove(letter)

        if done_count == len(segment_positions):
            break

    # make all entries letters and not lists
    for item in segment_positions:
        segment_positions[item] = segment_positions[item][0]

    print(segment_positions)
    # now we know the positions we can decode the output number
    output_amount = ""
    for number in output_signal:

        # skip decoding easy (unique) numbers
        if len(number) == 2:
            print("Decoded 1:", number)
            output_amount += "1"
        elif len(number) == 4:
            print("Decoded 4:", number)
            output_amount += "4"
        elif len(number) == 3:
            print("Decoded 3:", number)
            output_amount += "7"
        elif len(number) == 7:
            print("Decoded 8:", number)
            output_amount += "8"

        # else we need to decode using positions from the above dictionary
        else:
            print("UNDECODED number:", number)

            # have to decode numbers 3, 5, 6, 9

            # easy/unique ones to decode
            if segment_positions["LR"] not in number:
                print("Decoded 2")
                output_amount += "2"
            elif segment_positions["M"] not in number:
                print("Decoded 0")
                output_amount += "0"

            # else we actually need to decode it
            else:
                # list of what each number SHOULD contain, translated to the letters
                segment_3 = [segment_positions["T"], segment_positions["UR"], segment_positions["M"],
                                segment_positions["LR"], segment_positions["B"]]
                print(segment_3)


    break





    print(output_amount)




# NOTE
# Unique = 1(2), 4(4), 7(3), 8(7)

""""
number 9 may be only one we need
        elif len(number) == 2:    # number 1
            #print("Number 1")
            segment_positions["UR"] = number[0]
            segment_positions["LR"] = number[1]

        elif len(number) == 4:  # number 4
            #print("Number 4")
            segment_positions["UL"] = number[0]
            segment_positions["UR"] = number[1]
            segment_positions["M"]  = number[2]
            segment_positions["LR"] = number[3]

        elif len(number) == 3:  # number 7
            #print("Number 7")
            segment_positions["T"]  = number[0]
            segment_positions["UR"] = number[1]
            segment_positions["LR"] = number[2]
"""
