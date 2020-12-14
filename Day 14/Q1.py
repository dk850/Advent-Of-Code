def mask_value(mask, value):
    pos = 0

    # since this mask overwrites bits it is best to loop over the mask
    # rather than bitwise functions due to the X values
    for bit in mask:
        if bit == "X":
            pass
        elif bit == "0":
            value[pos] = "0"
        elif bit == "1":
            value[pos] = "1"
        pos += 1
    #print("New v:", value)
    return(value)

f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

# initialise memory as dictionary and parse input
mem = {}
for instruction in infile:
    if instruction[0:4] == "mask":
        mask = list(instruction.split('=')[1][1:])
        #print("Mask: ", mask)

    elif instruction[0:3] == "mem":
        # apply latest mask to value in instruction
        value = list('{0:036b}'.format(int(instruction.split('=')[1][1:])))
        masked_value = mask_value(mask, value)
        output_value = int("".join(str(x) for x in masked_value), 2) # turn binary list into integer
        #print("Masked value:", output_value)

        # add value to the memory address
        addr = int("".join(str(x) for x in instruction.split('=')[0] if x.isdigit() ))
        mem[addr] = output_value

sum = 0
for addr in mem:
    sum += mem[addr]
print("Final sum:", sum)
