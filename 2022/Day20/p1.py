f = open("example", "r")
input = [int(x) for x in f.read().splitlines()]
# print("IN:", input)
print()

# build id dictionary and initial list
numbers = {}  # { id/initial_position : instruction/number }
active_arrangement = []  # consists of number ID initially in order, to be mixed
for pos in range(len(input)):
    numbers[pos] = input[pos]
    active_arrangement.append(pos)


def printArrangement():
    print("ARRANGEMENT")
    print(active_arrangement)
    ln = ""
    for i in active_arrangement:
        ln += str(numbers[i]) + "  "
    print(ln)
    print()


# printArrangement()

# look at deque and rotate  * -1
"""
Python 3 - deques and comments
https://github.com/hugseverycat/aoc2022/blob/main/day20.py

I have one list that remains unchanged the whole time so that I can maintain the original order.

Then I have two deques: one which contains the values and is mixed around. Another deque contains the original indexes and is mixed around in an identical manner. Technically I probably only need the index deque, but I was having enough brain confusion with this puzzle that I wanted to stop writing things like my_list[some_other_list.index(my_list[i])] or whatever. Maybe later I will attempt to refactor.

Anyway, to perform the actual mixing, I grab the current index of the value I'm looking for from the current_index_list deque, delete that item from both deques, then rotate the deque by the value. Then I replace the item into both deques at the same index. So instead of moving the item, I move the whole list beneath the item.
"""

for id in range(len(numbers.keys())):
    print("ID:", id, "  VALUE:", numbers[id])

    ## Move id by its number value in the active arrangement
    o_idx = active_arrangement.index(id)
    print("Orig index:", o_idx)

    n_idx = o_idx + numbers[id]
    print("New index:", n_idx)

    if n_idx == 0:
        print("Base reshuffle")
        active_arrangement.append(active_arrangement.pop(o_idx))

    elif n_idx < 0:
        print("Underflow")
        r = n_idx % len(active_arrangement)  # people saying modulus needs to be -1
        print(len(active_arrangement), r)

        active_arrangement.insert(r, id)
        active_arrangement.pop(o_idx)

    elif n_idx > len(active_arrangement):
        print("Overflow")
        r = n_idx % len(active_arrangement)
        print(r)
        active_arrangement.insert(r + 1, active_arrangement.pop(o_idx))

    else:
        active_arrangement.insert(n_idx, active_arrangement.pop(o_idx))

    # printArrangement()
    print()


# get 1000, 2000, 3000 digits after 0
pos0 = [k for k, v in numbers.items() if v == 0][0]  # get id of the number 0 (unique)
print("1000:", numbers[active_arrangement[(1000 + pos0) % len(active_arrangement) - 1]])
print("2000:", numbers[active_arrangement[(2000 + pos0) % len(active_arrangement) - 1]])
print("3000:", numbers[active_arrangement[(3000 + pos0) % len(active_arrangement) - 1]])
