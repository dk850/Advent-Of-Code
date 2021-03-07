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

max_seat_id = 0
for seat in infile:
    row = decode_row(seat)
    col = decode_col(seat)
    seat_id = (row * 8) + col

    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)
