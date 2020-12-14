def mask_addr(mask, addr):
    pos = 0
    for bit in mask:
        if bit == "0":
            pass
        elif bit == "1":
            addr[pos] = "1"
        elif bit == "X":
            addr[pos] = "X"
        pos += 1
    return addr

def add_addr_possibilities(addr):
    global g_list_addrs

    # base case no more X in addr, add it to list
    if "X" not in addr:
        g_list_addrs.append(int("".join(str(x) for x in addr), 2))
        #return addrs
    else:
        #print("Fixing:", addr)

        # get index of first x and return array with the combinations
        index = addr.index("X")

        addr[index] = "0"
        addr0 = addr.copy()
        addr[index] = "1"
        addr1 = addr.copy()

        #print("0      ", addr0)
        #print("1      ", addr1)
        add_addr_possibilities(addr1)
        add_addr_possibilities(addr0)

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
        # apply latest mask to memory address in instruction
        bin_addr = list('{0:036b}'.format(int("".join(str(x) for x in instruction.split('=')[0] if x.isdigit()))))
        masked_addr = mask_addr(mask, bin_addr)

        # use global list to hold addresses
        # NOTE: couldnt get recursive output working properly this time. Need to revisit
        g_list_addrs = []
        add_addr_possibilities(masked_addr) # adds addrs to g_list_addrs

        # parse value
        value = int(instruction.split('=')[1][1:])
        #print("Value:", value)

        # add value to the memory address in list
        for addr in g_list_addrs:
            mem[addr] = value

sum = 0
for addr in mem:
    sum += mem[addr]
print("Final sum:", sum)
