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

def check_program(instructions):
    global g_program_counter
    global g_accumulator

    # reset global counters
    g_program_counter = 0
    g_accumulator = 0
    isValid = True

    # check same line isnt executed more than once
    executed_lines = []
    while True:
        executed_lines.append(g_program_counter)
        operand = instructions[g_program_counter][0]
        argument = instructions[g_program_counter][1]

        # if line executed more than once it fails as it is in infinite loop
        if compute(operand, argument) in executed_lines:
            isValid = False
            break

        # if the program counter tries to execute instruction exactly 1 after the final, it has finished successfully
        elif g_program_counter == len(instructions):
            isValid = True
            break

    #print("Accumulator Count:", g_accumulator, "- valid!" if isValid else "- invalid" )
    return isValid

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

# try changing each jmp to nop and each nop to jmp one by one to fix code
for instruction in range(len(instruction_list)):
    operand = instruction_list[instruction][0]

    # swap exactly 1 jmp or nop
    if operand == "jmp":
        instruction_list[instruction][0] = "nop"
    elif operand == "nop":
        instruction_list[instruction][0] = "jmp"

    # swap back if program isnt fixed
    if not check_program(instruction_list):
        if operand == "jmp":
            instruction_list[instruction][0] = "jmp"
        elif operand == "nop":
            instruction_list[instruction][0] = "nop"

    # otherwise program executed successfully
    else:
        print("Accumulator:", g_accumulator)
        break
