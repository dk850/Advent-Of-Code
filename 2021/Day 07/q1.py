from collections import Counter



def get_mode(int_list):
    # count occurances of each position and return the most common position (not the amount of times it appeared)
    return Counter(int_list).most_common(1)[0][0]


def get_fuel_cost(positions, goal):
    # get distance of each position from the goal position and add that as the fuel cost

    fuel_cost = 0
    for position in positions:
        fuel_cost += abs(position - goal)  # avoid negatives with abs

    return fuel_cost



# read in the crab positions
f = open("testlist.txt", "r")
crab_position = f.read().split(',')
crab_position = [int(x.strip()) for x in crab_position]

# get modal position and check the fuel cost of getting every crab there
#mode = get_mode(crab_position)
#best_fuel = get_fuel_cost(crab_position, mode)  # baseline

# start at min position and calculate upto max, store the best position
min_f = min(crab_position)
max_f = max(crab_position)
current = min_f
best_fuel = 50000000000  # start with large fuel to optimise
while current != max_f+1:
    fc = get_fuel_cost(crab_position, current)
    if fc < best_fuel:
        best_fuel = fc
    current += 1
print("Best fuel:", best_fuel)
