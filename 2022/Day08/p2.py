f = open("input", "r")
input = f.read().splitlines()

# Build dict of trees
trees={}  # (ROW, COL) = height
for row in range(len(input)):
    for col in range(len(input[0])):
        #print("("+str(row)+","+str(col)+")",input[row][col])
        trees[(row, col)] = input[row][col]
print(trees)
print()

# returns list of [up, down, left, right] viewing distance
def get_viewscore_matrix(coords, height):  # (ROW, COL), height
    # determine if the tree is at front of treeline, 0 visibility
    if 0 in coords or len(input[0])-1 in coords:  # grid is square
        return [0, 0, 0, 0]
    
    # check tree height
    row, col=coords
    my_size=trees[coords]
    print("CHECKING TREE:", coords, height, "size", my_size)
    
    up=row+1
    down=len(input)-row
    left=col+1
    right=len(input)-col    
    print(up-1,down-1,left-1,right-1)
    
    
    viewscore_matrix = [0, 0, 0, 0]  # up down left right. 0-visible, 1-hidden
    for i in range(1, up):
        t_size = trees[row-i, col]
        print("checking up", row-i, col, "=", t_size )
        if t_size >= my_size:
            viewscore_matrix[0] += 1  # add one to score if tree is SMALLER
            break
        else:
            viewscore_matrix[0] += 1  # add one to score if tree is SMALLER
            
    
    for i in range(1, down):
        t_size = trees[row+i, col]  # tree above
        print("checking dn", row+i, col, "=", t_size )
        if t_size >= my_size:
            viewscore_matrix[1] += 1  # add one to score if tree is SMALLER
            break
        else: 
            viewscore_matrix[1] += 1  # add one to score if tree is SMALLER
    
    for i in range(1, left):
        t_size = trees[row, col-i]  # tree above
        print("checking le", row, col-i, "=", t_size )
        if t_size >= my_size:
            viewscore_matrix[2] += 1  # add one to score if tree is SMALLER
            break
        else:
            viewscore_matrix[2] += 1  # add one to score if tree is SMALLER
    
    for i in range(1, right):
        t_size = trees[row, col+i]  # tree above
        print("checking ri", row, col+i, "=", t_size )
        if t_size >= my_size:
            viewscore_matrix[3] += 1  # add one to score if tree is SMALLER
            break 
        else:
            viewscore_matrix[3] += 1  # add one to score if tree is SMALLER
        
        
    print(viewscore_matrix)
    return viewscore_matrix
    
    
    
    
    
    
    
maxscore=0
for tree in trees:
    matrix=get_viewscore_matrix(tree, trees[tree])
    score=1
    for value in matrix:
        score *= value
    print("SCORE:", score)
    print()
    if score > maxscore:
        maxscore=score
print("MAX:", maxscore)