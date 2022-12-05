from collections import deque

f = open("input", "r")
input = f.read().splitlines()

# Parse input
start_config=[]
instructions=[]
for i in range(len(input)):
    if input[i] == "":
        instructions=input[i+1:]
        break
    start_config.append(input[i])
print(start_config)
print(instructions)


# Build deques
stacks={}
for i in range(int(start_config[-1][-1])):
    stacks[i]=deque()

for i in range(2, len(start_config)+1):  # loop over every line of instruction
    for stack in range(len(stacks)+1):  # find position of box
        if (stack*4)+1 > len(start_config[-i]):
            break
        box=start_config[-i][(stack*4)+1]
        if box != "" and box != " ":  # if real box assign to stack
            stacks[stack].append(box)
print()

# Function to move boxes by given amounts into other stacks
def move_box(box_from, box_to, stack_step):
    global stacks
    for step in range(1, stack_step+1):
        stacks[box_to-1].append(stacks[box_from-1].pop())  # -1 due to 0-based queues but 1-based steps


# Loop over instruction, parse, and call move box function
for ins in instructions:
    i_step=int(ins.replace('move ','').split(' from')[0])
    i_from=int(ins.split(' from ')[1].split(' to')[0])
    i_to=int(ins.split(' to ')[1])

    move_box(i_from, i_to, i_step)


# get top boxes string
out=""
for stack in stacks:
    out+=str(stacks[stack].pop())
print(out)
