# parse and read in the height map
f = open("input1.txt", "r")
input_heightmap = f.read().splitlines()
heightmap = [list(int(x) for x in x) for x in input_heightmap]  # separate each string into its own int element in the list


# go over each row in the table and figure out if it a low point
low_points = []
for row_pos in range(len(heightmap)):
    # setup row search variables to make code reading easier
    top_row    = 1 if row_pos == 0 else 0
    bottom_row = 1 if row_pos == (len(heightmap) - 1) else 0

    for col_pos in range(len(heightmap[row_pos])):
        # setup column search variables for easy code reading
        left_side = 1 if col_pos == 0 else 0
        right_side = 1 if col_pos == (len(heightmap[row_pos]) - 1) else 0
        position = heightmap[row_pos][col_pos]

        # for a top row
        if top_row:
            # top left
            if left_side:
                if (position < heightmap[row_pos][col_pos+1]) and \
                        (position < heightmap[row_pos+1][col_pos]):
                    low_points.append(position)
            # top right
            elif right_side:
                if (position < heightmap[row_pos][col_pos-1]) and \
                        (position < heightmap[row_pos+1][col_pos]):
                    low_points.append(position)
            # other tops
            else:
                if (position < heightmap[row_pos][col_pos-1]) and (position < heightmap[row_pos][col_pos+1]) and \
                        (position < heightmap[row_pos+1][col_pos]):
                    low_points.append(position)

        # for a bottom row
        elif bottom_row:
            # bottom left
            if left_side:
                if (position < heightmap[row_pos-1][col_pos]) and \
                        (position < heightmap[row_pos][col_pos+1]):
                    low_points.append(position)
            # bottom right
            elif right_side:
                if (position < heightmap[row_pos-1][col_pos]) and \
                        (position < heightmap[row_pos][col_pos-1]):
                    low_points.append(position)
            # other bottoms
            else:
                if (position < heightmap[row_pos-1][col_pos]) and \
                        (position < heightmap[row_pos][col_pos-1]) and (position < heightmap[row_pos][col_pos+1]):
                    low_points.append(position)

        # for a left side
        elif left_side:
            if (position < heightmap[row_pos-1][col_pos]) and \
                    (position < heightmap[row_pos][col_pos+1]) and \
                    (position < heightmap[row_pos+1][col_pos]):
                low_points.append(position)

        # for a right side
        elif right_side:
            if (position < heightmap[row_pos-1][col_pos]) and \
                    (position < heightmap[row_pos][col_pos-1]) and \
                    (position < heightmap[row_pos+1][col_pos]):
                low_points.append(position)

        # for any other (normal) position
        else:
            if (position < heightmap[row_pos-1][col_pos]) and \
                    (position < heightmap[row_pos][col_pos-1]) and (position < heightmap[row_pos][col_pos+1]) and \
                    (position < heightmap[row_pos+1][col_pos]):
                low_points.append(position)



# answer wants sum of risk level which is low point height + 1
sum = 0
for point in low_points:
    sum += 1 + point
print(sum)
