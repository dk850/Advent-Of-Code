f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

bus_timetable = infile[1].split(',')

bus_ids = []
for index in range(len(bus_timetable)):
    if bus_timetable[index].isdigit():
        bus_ids.append([int(bus_timetable[index]), index]) # [bus, offset_from_t]

# debug
if 0:
    print("Bus timetable:", bus_timetable)
    print("Bus IDs:")
    for id in bus_ids:
        print(id)
    print('\n')

# initialise needed variables
timestamp_t = 0
increment = 1
validity_index = 0
old_validity_index = 0

while True:
    timestamp_t += increment

    # since they are all prime numbers we can do this to validate and get the index where we are valid at
    for index in range(len(bus_ids)):
        a = (timestamp_t + bus_ids[index][1]) / bus_ids[index][0]
        if a.is_integer():
            validity_index = index
        else:
            break

    # if we have found the next valid matching bus timetable
    if validity_index > old_validity_index:
        old_validity_index = validity_index

        # we change the increment to be the LCM of where we are at as it is periodic
        increment = 1
        for i in range(validity_index):
            increment *= bus_ids[i][0]

    # if we have validated all bus ids then this is the first instance it is correct
    if validity_index == len(bus_ids)-1:
        print("Answer:", timestamp_t)
        break
