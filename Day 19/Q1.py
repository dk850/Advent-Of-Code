def decode_rule(rule):
    global global_rules
    valid_sequences = []
    #print("Decoding rule:", str(rule) + ":" + str(global_rules[rule]))

    # base case one length & letter
    if len(global_rules[rule]) == 1:
        if global_rules[rule][0] == "a":
            #print("Base case a")
            return "a"
        elif global_rules[rule][0] == "b":
            #print("Base case b")
            return "b"

        # if it is one length and not a letter then we recursively go down again to the next instruction
        else:
            valid_sequences.append(decode_rule(global_rules[rule][0]))
            #print("Valid Message for:", rule, valid_sequences)

    # else if it contains a pipe we can go 2 routes
    elif "|" in global_rules[rule]:
        pipe_pos = global_rules[rule].index("|")
        #print("Found pipe at:", str(pipe_pos) + ", split")

        # split and loop over both sides
        new_ruleL = global_rules[rule][0:pipe_pos]
        new_ruleR = global_rules[rule][pipe_pos+1:]

        valid_messageL = []
        valid_messageR = []
        for inner_rule in new_ruleL:
            valid_messageL.append(decode_rule(inner_rule))
        valid_sequences.append(valid_messageL)
        #print("Valid MessageL:", rule, valid_messageL)

        for inner_rule in new_ruleR:
            valid_messageR.append(decode_rule(inner_rule))
        valid_sequences.append(valid_messageR)
        #print("Valid MessageR:", rule, valid_messageR)

    # else recursively go down into another rule
    else:
        for inner_rule in global_rules[rule]:
            valid_sequences.append(decode_rule(inner_rule))

    #print("Sequence found:", rule, valid_sequences)
    return valid_sequences

def check_message_validity(message, valid_sequence):
    print("Checking message:", message)

    sequence_pos = 0
    while 1:

        #if the sequence only contains one letter the message must contain it at this position
        if len(valid_sequence[sequence_pos]) == 1:
            print("Checking for:", valid_sequence[sequence_pos])

            if message[sequence_pos] != valid_sequence[sequence_pos]:
                print("Invalid match")
                break
            else:
                print("Match")

        # if the sequence contains multiple options then we can take one path
        else:
            print(len(valid_sequence[sequence_pos]))
            for option in valid_sequence[sequence_pos]:
                print(option)

        sequence_pos += 1
        if sequence_pos == len(valid_sequence):
            break

f = open("example1.txt", "r")
infile = f.read().splitlines()
f.close()

# parse input into dict of rules and list of messages
global_rules = {}
messages = []
for line in infile:
    # ignore the seperator
    if line == '':
        pass

    # rules
    elif str(line[0]).isdigit():
        rule = line.split(':')
        rule_number = int(rule[0])
        rule = rule[1][1:].split(' ')

        fixed_rule = []
        for element in rule:
            if element.isdigit():
                fixed_rule.append(int(element))
            elif element == "\"a\"":
                fixed_rule.append("a")
            elif element == "\"b\"":
                fixed_rule.append("b")
            elif element == "|":
                fixed_rule.append("|")
        global_rules[rule_number] = fixed_rule
        #print("Added rule:", rules[rule_number], "pipe" if "|" in rules[rule_number] else "")

    # if not seperator or rule its a message
    else:
        messages.append([x for x in line]) # split string into list
        #print("Message:", line)

valid_sequence = decode_rule(0) # decode base rule to get full sequence
print("Valid sequence:", valid_sequence)

def depth(nested):
    instring = False
    count = 0
    depthlist = []
    for char in repr(nested):
        if char == '"' or char == "'":
            instring = not instring
        elif not instring and ( char == "[" or char == "(" ):
            count += 1
        elif not instring and ( char == "]" or char == ")" ):
            count -= 1
        depthlist.append(count)
    return(max(depthlist))

print(depth(valid_sequence))

valid_count = 0
for message in messages:
    if(check_message_validity(message, valid_sequence)):
        valid_count += 1
    break
#print(valid_count)


#base case for recursion on the valid list is only 2 options so if the list is length
# length one then it is base case so see if it matches positions in message if not then will
# need to check other side of the list and if that not return false so it can check other side all the
# recursive way up
