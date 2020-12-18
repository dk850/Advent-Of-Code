def left_right_maths(equation):
    # base

    if len(equation) == 3:
        total = int(equation[0])
        # there are only 2 operators, + and *
        if equation[1] == '*':
            total *= int(equation[2])
        else:
            total += int(equation[2])

    # else recursively add
    else:
        total = int(equation[-1])
        # there are only 2 operators, + and *
        if equation[-2] == '*':
            total *= int(left_right_maths(equation[:-2]))
        else:
            total += int(left_right_maths(equation[:-2]))

    print("Result:", total)
    return total

def do_maths(equation, size = 0):
    print("Main Equation:", equation)
    inner_equation = []
    skip = False
    count = 0

    # if no brackets we can just compute it
    if ("(" not in equation) and (")" not in equation):
        print("Base case")
        return int(left_right_maths(equation))

    # otherwise we need to find a matching bracket
    else:
        # loop over equation until we find the start of a bracket
        for pos in range(len(equation)):
            print("Inner Equation:", inner_equation)
            print(equation[pos])
            # we have already computed value below so skip x
            if skip > 0:
                print("skipping")
                skip -= 1
            # find bracket that matches singular bracket
            elif (equation[pos] == "("):
                print("found ( at", pos, "pos2in", range(pos+1, len(equation)))
                count += 1

                # look for matching )
                for pos2 in range(pos+1, len(equation)):
                    print("searching for matching ) count of (:", count, "searchstring:", equation[pos:len(equation)])
                    print(equation[pos2])
                    if equation[pos2] == "(":
                        count += 1
                        print("Found another (. Count:", count)
                    elif equation[pos2] == ")":
                        print("Found a ). check if matches")
                        count -= 1

                        # if we have found matching bracket, skip that many positions and add sum to inner equation
                        if count == 0:
                            print("count is 0. Matches")
                            skip = len(equation[pos:pos2])
                            intotal = do_maths(equation[pos+1:pos2])
                            print("adding:", intotal)
                            print("skipping", skip)
                            inner_equation.append(str(intotal))
                            break
            else:
                inner_equation.append(equation[pos])
        print("fell out")
        return do_maths(inner_equation)
f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

sum = 0
for line in infile:
    equation = [x for element in line.split() for x in element]

    sum += do_maths(equation)
print("End sum:", sum)
