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
    # make sure the point is valid
    if not ((point[0] < len(map)) and (point[0] >= 0)):
        return
    if not ((point[1] < len(map[0])) and (point[1] >= 0)):
        return


    # if the point is a 9 we have got to the end of a basin
    to_check = map[point[0]][point[1]]
    if to_check == 9:
        return basin_points


    # otherwise add the current point to the list and keep searching
    else:
        basin_points.append(point)

        # setup search variables to make code reading easier
        top_row    = 1 if point[0] == 0 else 0
        bottom_row = 1 if point[0] == (len(map) - 1) else 0
        left_side = 1 if point[1] == 0 else 0
        right_side = 1 if point[1] == (len(map[point[0]]) - 1) else 0

        new_points = []
        if top_row:
            if left_side:
                if [point[0], point[1]+1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]+1], basin_points))  # right
                if [point[0]+1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]+1, point[1]], basin_points))  # down
            if right_side:
                if [point[0], point[1]-1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]-1], basin_points))  # left
                if [point[0]+1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]+1, point[1]], basin_points))  # down
            else:  # middle of top row
                if [point[0], point[1]+1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]+1], basin_points))  # right
                if [point[0], point[1]-1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]-1], basin_points))  # left
                if [point[0]+1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]+1, point[1]], basin_points))  # down
        if bottom_row:
            if left_side:
                if [point[0], point[1]+1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]+1], basin_points))  # right
                if [point[0]-1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]-1, point[1]], basin_points))  # up
            if right_side:
                if [point[0], point[1]-1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]-1], basin_points))  # left
                if [point[0]-1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]-1, point[1]], basin_points))  # up
            else:  # middle of top row
                if [point[0], point[1]+1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]+1], basin_points))  # right
                if [point[0], point[1]-1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]-1], basin_points))  # left
                if [point[0]-1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]-1, point[1]], basin_points))  # up
        else:  # not top or bottom row
            if left_side:
                if [point[0], point[1]+1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]+1], basin_points))  # right
                if [point[0]+1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]+1, point[1]], basin_points))  # down
                if [point[0]-1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]-1, point[1]], basin_points))  # up
            if right_side:
                if [point[0], point[1]-1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]-1], basin_points))  # left
                if [point[0]+1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]+1, point[1]], basin_points))  # down
                if [point[0]-1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]-1, point[1]], basin_points))  # up
            else:  # middle of top row
                if [point[0], point[1]+1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]+1], basin_points))  # right
                if [point[0], point[1]-1] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0], point[1]-1], basin_points))  # left
                if [point[0]+1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]+1, point[1]], basin_points))  # down
                if [point[0]-1, point[1]] not in basin_points:
                    new_points.append(r_find_basin(map, [point[0]-1, point[1]], basin_points))  # up


        # add new points to the basin list
        for point_list in new_points:
            if point_list is None:
                continue
            for point in point_list:
                if point is None:
                    continue
                if point not in basin_points:  # avoid duplicates
                    basin_points.append(point)
        # note this could maybe be a function that we cann after we get values from the recursive function to add to the basin
        #      before checking further values - see if this is quick enough first

        return basin_points



# parse and read in the height map
f = open("input1.txt", "r")
input_heightmap = f.read().splitlines()
heightmap = [list(int(x) for x in x) for x in input_heightmap]  # separate each string into its own int element in the list

# get list of low point heights and their position [height, [pos]]
low_points = find_low_points(heightmap)

# loop over each low point and determine the size of the basin and add to list
basin_sizes = []
for point, position in low_points:
    basin_points = []
    bpoints = r_find_basin(heightmap, position, basin_points)
    basin_sizes.append(len(bpoints))

# answer wants us to multiply the three largest basins
basin_sizes.sort()
ans = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
print(ans)
