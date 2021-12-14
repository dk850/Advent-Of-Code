# used to print a board
def display_board(board):
    print()
    for row in board:
        print(row)
    print()

# used to check if a board contains a number and if it does we change the 0 signifier to a 1 to show it is filled
def fill_board(board, draw_number):
    for row in board:
        for number in row:
            if draw_number in number:
                new_number = ['x', number[1]]
                row[row.index(number)] = new_number
                return 1  # success, stop here
    return 0  # failed


# used to see if we have a complete bingo (all 5 1's horizontal or vertical)
def check_board(board):

    # check each row (always 5 long)
    for row in board:
        if (row[0][0] == 'x') and (row[1][0] == 'x') and (row[2][0] == 'x') and \
                (row[3][0] == 'x') and (row[4][0] == 'x'):
            print("BINGO")
            return 1

    # check each column (5 tall)
    for i in range(5):
        if (board[0][i][0] == 'x') and (board[1][i][0] == 'x') and (board[2][i][0] == 'x') and \
                (board[3][i][0] == 'x') and (board[4][i][0] == 'x'):
            print("BINGO")
            return 1

    return 0


f = open("input1.txt", "r")
subsystem = f.read().splitlines()

# get the initial release order from the subsystem file
release_order = [int(x) for x in subsystem[0].split(',')]
print(release_order)

# build the boards
subsystem = subsystem[2:]
boards = [[]]
boards_index = 0

# get the list of strings out of the subsyetm list and order in a boards list
for element in subsystem:
    if element == '':
        boards.append([])
        boards_index += 1
    else:
        boards[boards_index].append(element)

# split board row strings seperated by spaces into elements of int
new_boards = []
for board in boards:
    new_board = []
    for row in board:
        new_board.append([int(x) for x in row.split(' ') if x])  # if x not empty then add the element as an int
    new_boards.append(new_board)
boards = new_boards  # done, now overwrite original variable

# add another element to each value on each board to signify if the number has came out yet or not
new_boards = []
for board in boards:
    new_board = []
    for row in board:
        new_row = []
        for element in row:
            new_element = ['o', element]
            new_row.append(new_element)
        new_board.append(new_row)
    new_boards.append(new_board)
boards = new_boards


# draw numbers
bingo = -1  # to hold the winning number and board
for number in release_order:
    print("Drew:", number)

    # put number on each board
    for board in boards:
        fill_board(board, number)
        if check_board(board) == 1:  # check if we have bingo
            bingo = [number, board]

    if bingo != -1:
        print()
        break


# get answer to question
unmarked_total = 0
for row in bingo[1]:
    for element in row:
        if element[0] == 'o':  # if element in row of winning board is unmarked (i.e. not X, not drawn) add to total
            unmarked_total += element[1]

print(unmarked_total*bingo[0])  # get answer
