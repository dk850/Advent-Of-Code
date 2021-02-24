def move_toboggan(position, topology, right=3, down=1):
    # Deal with X position due to repeating topology
    posY = position[1]
    posXModifier = position[0] // 31
    posX = position[0] - (31*posXModifier)
    #print("Position:", position)
    #print("PosX:", posX)
    #print("PosXModifier:", posXModifier)
    #print("PosY:", posY)

    current_icon = topology[posY][posX]
    #print("Current Icon:", current_icon)

    # Deal with any potential loops here whilst looking for next icon
    if posX+right > 30:
        #print("Loop Encountered")
        posXModifier += 1
        posX = (position[0] + right) - (31*posXModifier)
    else:
        posX = (position[0] + right)
    #print(topology[posY])
    posY = posY + down
    #print("New posX:", posX)
    #print("New posY:", posY)

    # Find new icon
    next_icon = topology[posY][posX]
    #print(topology[posY])
    #print("New Icon:", next_icon)

    # Return updated position and if there is a tree
    if next_icon == "#":
        #print("Tree Here")
        return ((posX, posY), 1)
    else:
        return ((posX, posY), 0)

f = open("input.txt", "r")
forest = f.read().splitlines()
f.close()

position = (0, 0)
tree_count = 0
for i in range(5):
    print(i)
for row in range(len(forest)-1):
    #print("Current Position:", position)
    #(position,tree) = move_toboggan(position, forest)
    tree_count += tree
#print("Position:", position, "Tree Count:", tree_count)
