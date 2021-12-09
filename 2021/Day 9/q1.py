# parse and read in the notes and the output
f = open("input1.txt", "r")
note_lines = f.read().splitlines()
note_lines = [x.split(' | ') for x in note_lines]  # split delimiter
note_lines = [[note.split(' '), output.split(' ')] for (note, output) in note_lines]  # split on spaces

# part 1 only wants to deal with unique values in the output section
# check for lengths of 2, 4, 3, or 7 in the output
unique_values = 0
for recorded_signal in note_lines:
    output_signal = recorded_signal[1]

    for number in output_signal:
        if (len(number) == 2) or (len(number) == 4) or (len(number) == 3) or (len(number) == 7):
            unique_values += 1

print(unique_values)

# NOTE
# Unique = 1(2), 4(4), 7(3), 8(7)
