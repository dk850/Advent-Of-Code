# return = (True/False, Swap). True = has been a swap
def determine_localality(layout, seat_row, seat_col):
    lSide = rSide = False
    top = bottom = False
    empty = occupied = floor = False

    # if seat is occupied or not
    seat_state = layout[seat_row][seat_col]
    if seat_state == '#':
        occupied = True
    elif seat_state == '.':
        floor = True
        #print("Keep as", seat_state)
        return (False, seat_state)
    elif seat_state == 'L':
        empty = True
    else:
        print("Error") # shouldnt get here on valid input

    # NOTE: can collapse these statments into the checking below but this makes it more readable
    # if the seat is on the top or bottom
    if (seat_row == 0):
        top = True
    elif (seat_row == len(layout)-1):
        bottom = True

    # if the seat is on the side
    if (seat_col == 0):
        lSide = True
    elif (seat_col == len(layout[0])-1):
        rSide = True


    # count first seats this seat can see that are occupied
    occupied_count = 0

    # check for seats above seat
    if not top:
        for seat in range(1, len(layout)):
            if seat_row-seat == -1:
                break
            elif layout[seat_row-seat][seat_col] == '#':
                occupied_count += 1
                break
            elif layout[seat_row-seat][seat_col] == 'L':
                break

    # check for seats below seat
    if not bottom:
        for seat in range(1, len(layout)):
            if seat_row+seat == len(layout):
                break
            elif layout[seat_row+seat][seat_col] == '#':
                occupied_count += 1
                break
            elif layout[seat_row+seat][seat_col] == 'L':
                break

    # check seats left of the seat
    if not lSide:
        for seat in range(1, len(layout[0])):
            if seat_col-seat == -1:
                break
            elif layout[seat_row][seat_col-seat] == '#':
                occupied_count += 1
                break
            elif layout[seat_row][seat_col-seat] == 'L':
                break

    # check seats right of the seat
    if not rSide:
        for seat in range(1, len(layout[0])):
            if seat_col+seat == len(layout[0]):
                break
            elif layout[seat_row][seat_col+seat] == '#':
                occupied_count += 1
                break
            elif layout[seat_row][seat_col+seat] == 'L':
                break

    # check upper left diagonal
    if not top:
        if not lSide:
            for seat in range(1, 1000):
                if (seat_row-seat == -1) | (seat_col-seat == -1):
                    break
                elif layout[seat_row-seat][seat_col-seat] == '#':
                    occupied_count += 1
                    break
                elif layout[seat_row-seat][seat_col-seat] == 'L':
                    break

    # check upper right diagonal
    if not top:
        if not rSide:
            for seat in range(1, 1000):
                if (seat_row-seat == -1) | (seat_col+seat == len(layout[0])):
                    break
                elif layout[seat_row-seat][seat_col+seat] == '#':
                    occupied_count += 1
                    break
                elif layout[seat_row-seat][seat_col+seat] == 'L':
                    break

    # check lower left diagonal
    if not bottom:
        if not lSide:
            for seat in range(1, 1000):
                if (seat_row+seat == len(layout)) | (seat_col-seat == -1):
                    break
                elif layout[seat_row+seat][seat_col-seat] == '#':
                    occupied_count += 1
                    break
                elif layout[seat_row+seat][seat_col-seat] == 'L':
                    break

    # check lower right diagonal
    if not bottom:
        if not rSide:
            for seat in range(1, 1000):
                if (seat_row+seat == len(layout)) | (seat_col+seat == len(layout[0])):
                    break
                elif layout[seat_row+seat][seat_col+seat] == '#':
                    occupied_count += 1
                    break
                elif layout[seat_row+seat][seat_col+seat] == 'L':
                    break
    #print("Occupied_count:", occupied_count)

    # Rule 1
    if empty & (occupied_count == 0):
        #print("Replace with #")
        return (True, '#')

    # Rule 2
    if occupied & (occupied_count > 4):
        #print("Replace with L")
        return (True, 'L')

    # Rule 3
    else:
        #print("Keep the same", seat_state)
        return (False, seat_state)

def get_occupied_count(layout):
    occupied_count = 0

    for row in layout:
        # only check rows with # in to speed it up slightly
        if '#' in row:
            occupied_count += row.count('#')
    return occupied_count

f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

# debug
if 0:
    print("Layout:")
    for row in infile:
        print(row)
    print("\n")

# repeat until nothing changes
repeat = True
old_layout = infile.copy()
new_layout = []
final_layout = []
while repeat:
    repeat_count = 0

    for row in range(len(old_layout)):
        new_row = ['F'] * len(old_layout[0])

        for col in range(len(old_layout[0])):
            value = determine_localality(old_layout, row, col)
            new_row[col] = value[1]

            if value[0] == True:
                repeat_count += 1

        new_layout.append(new_row)

    # debug
    if 0:
        print("New layout:")
        for row in new_layout:
            print(row)
        print("\n")

    # if nothing has changed, we are done
    if repeat_count == 0:
        final_layout = new_layout.copy()
        repeat = False
    else:
        old_layout = new_layout.copy()
        new_layout.clear()

# debug
if 0:
    print("Final layout:")
    for row in final_layout:
        print(row)
    print("\n")

print("Occupied seats:", get_occupied_count(final_layout))
