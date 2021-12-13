def find_low_points(map):
    # go over each row in the table and figure out if it a low point
    low_points = []
    for row_pos in range(len(map)):
        # setup row search variables to make code reading easier
        top_row    = 1 if row_pos == 0 else 0
        bottom_row = 1 if row_pos == (len(map) - 1) else 0

        for col_pos in range(len(map[row_pos])):
            # setup column search variables for easy code reading
            left_side = 1 if col_pos == 0 else 0
            right_side = 1 if col_pos == (len(map[row_pos]) - 1) else 0
            height = map[row_pos][col_pos]

            # for a top row
            if top_row:
                # top left
                if left_side:
                    if (height < map[row_pos][col_pos+1]) and \
                            (height < map[row_pos+1][col_pos]):
                        low_points.append([height, [row_pos, col_pos]])
                # top right
                elif right_side:
                    if (height < map[row_pos][col_pos-1]) and \
                            (height < map[row_pos+1][col_pos]):
                        low_points.append([height, [row_pos, col_pos]])
                # other tops
                else:
                    if (height < map[row_pos][col_pos-1]) and (height < map[row_pos][col_pos+1]) and \
                            (height < map[row_pos+1][col_pos]):
                        low_points.append([height, [row_pos, col_pos]])

            # for a bottom row
            elif bottom_row:
                # bottom left
                if left_side:
                    if (height < map[row_pos-1][col_pos]) and \
                            (height < map[row_pos][col_pos+1]):
                        low_points.append([height, [row_pos, col_pos]])
                # bottom right
                elif right_side:
                    if (height < map[row_pos-1][col_pos]) and \
                            (height < map[row_pos][col_pos-1]):
                        low_points.append([height, [row_pos, col_pos]])
                # other bottoms
                else:
                    if (height < map[row_pos-1][col_pos]) and \
                            (height < map[row_pos][col_pos-1]) and (height < map[row_pos][col_pos+1]):
                        low_points.append([height, [row_pos, col_pos]])

            # for a left side
            elif left_side:
                if (height < map[row_pos-1][col_pos]) and \
                        (height < map[row_pos][col_pos+1]) and \
                        (height < map[row_pos+1][col_pos]):
                    low_points.append([height, [row_pos, col_pos]])

            # for a right side
            elif right_side:
                if (height < map[row_pos-1][col_pos]) and \
                        (height < map[row_pos][col_pos-1]) and \
                        (height < map[row_pos+1][col_pos]):
                    low_points.append([height, [row_pos, col_pos]])

            # for any other (normal) position
            else:
                if (height < map[row_pos-1][col_pos]) and \
                        (height < map[row_pos][col_pos-1]) and (height < map[row_pos][col_pos+1]) and \
                        (height < map[row_pos+1][col_pos]):
                    low_points.append([height, [row_pos, col_pos]])


    return low_points



def r_find_basin(map, point, basin_points):
    1+1



# parse and read in the height map
f = open("testlist.txt", "r")
input_heightmap = f.read().splitlines()
heightmap = [list(int(x) for x in x) for x in input_heightmap]  # separate each string into its own int element in the list

low_points = find_low_points(heightmap)

# answer wants sum of risk level which is low point height + 1
sum = 0
print(low_points)
for point, _ in low_points:
    sum += 1 + point
print(sum)
