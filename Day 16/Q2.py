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

def get_valid_tickets(ticket_list):
    # discard invalid tickets
    valid_tickets = []
    for ticket in nearby_tickets:
        valid = find_valid_values(rules, ticket)
        # if each value valid
        if len(valid) == len(ticket):
            valid_tickets.append(ticket)
    return valid_tickets

def remove_pos_from_list(pos, ticket_list):
    for key in ticket_list:
        if len(ticket_list[key]) != 1:
            if pos in ticket_list[key]:
                ticket_list[key].remove(pos)
    return ticket_list

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

valid_tickets = get_valid_tickets(nearby_tickets)

# debug prints
#print("Rules:", rules)
#print("My ticket:", my_ticket)
#print("Nearby tickets:", nearby_tickets)
#print("Valid tickets:", valid_tickets)
#print()

# get dictionary of rules and their ranges
possible_rules = {}
for rule in rules:
    rule_name = rule.split(':')[0]
    part = rule.split(':')[1][1:].split(' or ')
    # add ranges to list
    possible_rules[rule_name] = [[int(part[0].split('-')[0]), int(part[0].split('-')[1])], \
                            [int(part[1].split('-')[0]), int(part[1].split('-')[1])]]

# find what position matches what rule name
ticket_positions = {} # rule_name : position_in_ticket_range
for rule in possible_rules:
    ticket_positions[rule] = list(x for x in range(len(valid_tickets[0])))
#print(ticket_positions)

for rule in possible_rules:

    for ticket in valid_tickets:
        #print("Next ticket:", ticket)

        for position in range(len(ticket)):
            #print("Checking:", ticket[position], "in", possible_rules[rule][0], possible_rules[rule][1])

            # if this position satisfies the rule ranges
            if ((ticket[position] >= possible_rules[rule][0][0]) & (ticket[position] <= possible_rules[rule][0][1])) | \
                (ticket[position] >= possible_rules[rule][1][0]) & (ticket[position] <= possible_rules[rule][1][1]):
                pass
            else:
                #print("Position:", position, "cant be", rule)
                ticket_positions[rule].remove(position)
                #print(ticket_positions)
                break

# loop over ticket_positions and if a key only has one positional value, it can be removed from all other keys
current_list = ticket_positions
found_positions = []
while True:
    singular_tickets = 0

    for key in current_list:
        if len(current_list[key]) == 1:
            if current_list[key] not in found_positions:
                found_positions.append(current_list[key][0])
                singular_tickets += 1
                current_list = remove_pos_from_list(current_list[key][0], current_list)

    # if every key has 1 value (thankfully this is the case with my actual input) break the loop
    if singular_tickets == len(current_list):
        for key in current_list:
            # print my ticket to answer question
            print(key, my_ticket[current_list[key][0]])
        break


print("Final multiplication:", 101*131*79*71*73*67)



















#
