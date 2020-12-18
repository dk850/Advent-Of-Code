def left_right_maths(equation):
    # only 2 operands are in the puzzle input (+, *) so it makes this easier
    # but in Q2 + comes before * so we have to loop over the equation
    #print("Input equation:", equation)

    # base cases equation only consists of + or *
    if ('+' in equation) and ('*' not in equation):
        total = 0
        for element in equation:
            if str(element).isdigit():
                total += int(element)

    elif ('+' not in equation) and ('*' in equation):
        total = 1
        for element in equation:
            if str(element).isdigit():
                total *= int(element)

    # loop over equation and do any additions
    else:
        pos = 0
        while pos < len(equation):
            if equation[pos] == "+":
                equation[pos] = int(equation[pos-1]) + int(equation[pos+1])
                del equation[pos-1]
                del equation[pos] # this works since we just removed a position it is effectively the +1 from above
            pos += 1

        # use recursion to condense remaining equation
        total = left_right_maths(equation)

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
                            #print("Doesnt match")
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
