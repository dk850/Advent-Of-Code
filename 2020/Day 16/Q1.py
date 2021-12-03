def find_valid_values(rules, ticket): # returns list of valid values for the ticket
    ranges = []
    accepted_values = []

    # get acceptable ranges from rules
    for rule in rules:
        part = rule.split(':')[1][1:].split(' or ')
        # add ranges to list
        ranges.append([int(part[0].split('-')[0]), int(part[0].split('-')[1])])
        ranges.append([int(part[1].split('-')[0]), int(part[1].split('-')[1])])

    for value in ticket:
        for range in ranges:
            if (value >= range[0]) & (value <= range[1]):
                accepted_values.append(value)
                break
    return accepted_values

f = open("input.txt", "r")
infile = f.read().split('\n')
f.close()

# parse ticket rules
rules = []
nearby_tickets = []
part = 0

for line in infile:

    if line == '':
        part += 1

    # get rules
    elif part == 0:
        rules.append(line)

    # get my ticket
    elif part == 1:
        if line != "your ticket:":
            my_ticket = list(map(int, line.split(',')))

    # get nearby tickets
    elif part == 2:
        if line != "nearby tickets:":
            nearby_tickets.append(list(map(int, line.split(','))))

#print("Rules:", rules)
#print("My ticket:", my_ticket)
#print("Nearby tickets:", nearby_tickets)
#print()

sum = 0
for ticket in nearby_tickets:
    valid = find_valid_values(rules, ticket)

    # check if a value in the ticket is invalid and sum it
    for value in ticket:
        if value not in valid:
            sum += value

print("Ticket scanning error rate:", sum)
