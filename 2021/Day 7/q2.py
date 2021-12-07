def get_fuel_cost(positions, goal):
    # part 2 means fuel cost is non-linear so must adjust this function to account for that

    fuel_cost = 0
    for position in positions:

        # each position costs 1 more to move there than the previous position so we can * it by a value
        position_cost = 0
        for i in range(abs(position - goal)+1):  # avoid negatives with abs
            position_cost += 1 * i
        fuel_cost += position_cost  # add position cost to the total fuel cost

        #fuel_cost += (0.5 * abs(position - goal)) * (abs(position - goal)+1)
        # NOTE : The above commented out line is a more optimal solution, it is the pure maths instead of that for loop above to save so much time
        #        The for loop performs a 0.5n(n+1) so can be sped up massively

        # if our current cost is already worse than the best fuel then no point in carrying on
        if fuel_cost > best_fuel:
            return fuel_cost

    return fuel_cost


# read in the crab positions
f = open("input1.txt", "r")
crab_position = f.read().split(',')
crab_position = [int(x.strip()) for x in crab_position]


# start at min position and calculate upto max, store the best position
min_f = min(crab_position)
max_f = max(crab_position)
current = min_f
best_fuel = 50000000000  # start with large fuel to optimise
# NOTE : this can probably be optomised by further analysis but this currently takes ~17s which is acceptable

while current != max_f+1:
    fc = get_fuel_cost(crab_position, current)
    if fc < best_fuel:
        best_fuel = fc
    current += 1

# print answer - cheapest fuel
print("Best fuel:", best_fuel)
