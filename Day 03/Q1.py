def move_toboggan(position, topology, right=3, down=1):
    # Deal with X position due to repeating topology
    posY = position[1] + down
    posXModifier = position[0] // 31
    posX = position[0] - (31*posXModifier)

    # Deal with any potential loops here whilst looking for next icon
    if posX+right > 30:
        posXModifier += 1
        posX = (position[0] + right) - (31*posXModifier)
    else:
        posX = (position[0] + right)
    icon = topology[posY][posX]

    # Return updated position and if there is a tree
    if icon == "#":
        return ((posX, posY), 1)
    else:
        return ((posX, posY), 0)

f = open("input.txt", "r")
forest = f.read().splitlines()
f.close()

position = (0, 0)
tree_count = 0

for row in range(len(forest)-1):
    (position,tree) = move_toboggan(position, forest)
    tree_count += tree
print("Tree Count:", tree_count)
