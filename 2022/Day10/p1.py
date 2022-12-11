f = open("input", "r")
input = f.read().splitlines()
input = [x.split(' ') for x in input ]  # split input on , to separate it easier

clock = 1
x_reg = 1
monitor_clock = [20, 60, 100, 140, 180, 220]  # times we need signal strength
output = 0  # final output sum

for line in input:
    # calculate instruction
    if line[0] == "noop":
        clock += 1
    elif line[0] == "addx":
        clock += 1
    
    # addx takes 2 cycles so clock must be checked for value twice
    if clock in monitor_clock and line[0] == "addx":
        output += clock * x_reg
    if line[0] == "addx":
        x_reg += int(line[1])
        clock += 1
    
    # final monitor value check
    if clock in monitor_clock:
        output += clock * x_reg

print(output)