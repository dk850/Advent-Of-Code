# Use binary to decode seat rows F=0 B=1
def decode_row(seat):
    #print("Seat:", seat[0:7])
    row = ""
    for i in range(7):
        #print("Loop:", i, seat[i])
        if seat[i] == "F":
            row += "0"
        elif seat[i] == "B":
            row += "1"
    return int(row, 2)

# Use binary to decode seat columns L=0 R=1
def decode_col(seat):
    seat = seat[7:10]
    #print("Seat:", seat)
    col = ""
    for i in range(3):
        if seat[i] == "L":
            col += "0"
        elif seat[i] == "R":
            col += "1"
    return int(col, 2)

f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

# Decode bording passes * find maximum seat id
max_seat_id = 0
seat_ids = []
for seat in infile:
    row = decode_row(seat)
    col = decode_col(seat)
    seat_id = (row * 8) + col

    seat_ids.append(seat_id)
    if seat_id > max_seat_id:
        max_seat_id = seat_id

# Find which seat is missing from the ordering
seat_ids.sort()
pos = 0
for i in range(32, max_seat_id+1):
    if seat_ids[pos] != i:
        print(i)
        break
    pos += 1

# Then to double check:
#print(seat_ids)
