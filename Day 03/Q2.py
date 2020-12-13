def move_toboggan(position, topology, right=3, down=1):
    # Deal with X position due to repeating topology
    posY = position[1]
    posXModifier = position[0] // 31
    posX = position[0] - (31*posXModifier)

    # Deal with any potential loops here whilst looking for next icon
    if posX+right > 30:
        posXModifier += 1
        posX = (posX + right) - (31*posXModifier)
    else:
        posX = (posX + right)

    # Do not allow Y to overflow list
    if posY+down > len(topology):
        return ((posX, posY), 0)
    else:
        posY = posY + down
    icon = topology[posY][posX]

    # Return updated position and if there is a tree
    if icon == "#":
        return ((posX, posY), 1)
    else:
        return ((posX, posY), 0)

def get_tree_count(forest, right, left):
    tree_count = 0
    position = (0, 0)

    for row in range(len(forest)-1):
        (position,tree) = move_toboggan(position, forest, right, left)
        tree_count += tree

    return tree_count

f = open("input.txt", "r")
forest = f.read().splitlines()
f.close()

position = (0, 0)
tree_counts = [0, 0, 0, 0, 0]

tree_counts[0] = get_tree_count(forest, 1, 1)
tree_counts[1] = get_tree_count(forest, 3, 1)
tree_counts[2] = get_tree_count(forest, 5, 1)
tree_counts[3] = get_tree_count(forest, 7, 1)
tree_counts[4] = get_tree_count(forest, 1, 2)
print("Tree Counts:", tree_counts)

print("Multiplied:", tree_counts[0]*tree_counts[1]*tree_counts[2]*tree_counts[3]*tree_counts[4])
