def left_right_maths(equation):
    # only 2 operands are in the puzzle input (+, *) so it makes this easier

    # base case only 2 ints in equation so add/multiply left to right
    if len(equation) == 3:
        total = int(equation[0])
        if equation[1] == '*':
            total *= int(equation[2])
        else:
            total += int(equation[2])

    # else recursively put rightmost value and its operator with the leftmost side of the list
    else:
        total = int(equation[-1])
        if equation[-2] == '*':
            total *= int(left_right_maths(equation[:-2]))
        else:
            total += int(left_right_maths(equation[:-2]))

    #print("Result:", total)
    return total

def do_maths(equation):
    #print("Main Equation:", equation)
    inner_equation = []
    open_bracket_count = 0
    main_loop_pos = 0

    # base case no brackets
    if ("(" not in equation) and (")" not in equation):
        answer = int(left_right_maths(equation))
        #print("Base case:", answer)
        return answer

    # otherwise we need to find a matching bracket pair
    else:
        # go over equation using a while loop so we can skip parts faster
        while main_loop_pos < len(equation):
            #print("Inner Equation:", inner_equation)
            #print("Checking:", equation[main_loop_pos])

            # if we are trying to add a ( to the equation, we instead look for a matching )
            if (equation[main_loop_pos] == "("):
                #print("( found at position", main_loop_pos)
                open_bracket_count += 1

                # loop over remainder of equation only
                #print("Checking for matching ) in:", equation[main_loop_pos:len(equation)])
                for bracket_search_pos in range(main_loop_pos+1, len(equation)):
                    #print("Checking:", equation[bracket_search_pos])

                    # if we find another ( then the next ) wont match the first so we keep a count
                    if equation[bracket_search_pos] == "(":
                        open_bracket_count += 1
                        #print("( total:", open_bracket_count)

                    elif equation[bracket_search_pos] == ")":
                        open_bracket_count -= 1

                        # 0 count means we have found the matching bracket
                        if open_bracket_count == 0:
                            #print("Matches")
                            # recursively check this inner equation for more brackets and put base case in inner equation
                            inner_equation.append(str(do_maths(equation[main_loop_pos+1:bracket_search_pos])))

                            # increase main loop position by size of bracketed equation
                            main_loop_pos += len(equation[main_loop_pos:bracket_search_pos]) + 1

                            # stop the inner for loop as we have found the matching brackets
                            break
                        #else:
                        #    print("Doesnt match")
            else:
                # otherwise just add the value to the inner equation and increase loop count
                inner_equation.append(equation[main_loop_pos])
                main_loop_pos += 1

        return do_maths(inner_equation)

f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

sum = 0
for line in infile:
    equation = [x for element in line.split() for x in element]

    sum += do_maths(equation)
print("End sum:", sum)
