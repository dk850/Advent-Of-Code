f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

arrival_time = int(infile[0])
bus_ids = [int(x) for x in infile[1].split(',') if x.isdigit()]

# debug
if 0:
    print("Arrival time:", arrival_time)
    print("Bus IDs:")
    for id in bus_ids:
        print(id)
    print('\n')

earliest_bus = [arrival_time*100000, 69] # [difference, ID]

for bus in bus_ids:
    current_bus_time = bus
    while current_bus_time < arrival_time:
        current_bus_time += bus
    bus_difference = current_bus_time - arrival_time

    if earliest_bus[0] > bus_difference:
        earliest_bus = [bus_difference, bus]

print("Earliest bus:", earliest_bus)
print("Answer:", earliest_bus[0] * earliest_bus[1])
