def compute(operand, argument):
    global g_program_counter
    global g_accumulator

    # no operation
    if operand == "nop":
        g_program_counter += 1

    # global accumulator
    elif operand == "acc":
        if argument[0] == "+":
            g_accumulator += int(argument[1:])
        else:
            g_accumulator -= int(argument[1:])
        g_program_counter += 1

    # jump
    elif operand == "jmp":
        if argument[0] == "+":
            g_program_counter += int(argument[1:])
        else:
            g_program_counter -= int(argument[1:])

    return g_program_counter

f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

# form input correctly
instruction_list = []
for instruction in infile:
    instruction_list.append([instruction[0:3], instruction[4:]])

# for debug
if 0:
    print("Instructions:")
    for instruction_number in instruction_list:
        print(instruction_number)
    print("\n")

# declare global variables
g_program_counter = 0
g_accumulator = 0

# loop until same line executed more than once
executed_lines = []
while True:
    executed_lines.append(g_program_counter)
    operand = instruction_list[g_program_counter][0]
    argument = instruction_list[g_program_counter][1]

    if(compute(operand, argument) in executed_lines):
        break

print("Accumulator Count:", g_accumulator)
