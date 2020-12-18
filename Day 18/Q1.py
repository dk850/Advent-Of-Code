def left_right_maths(equation):
    # base
    if len(equation) == 1:
        total = int(equation[0])
    elif len(equation) == 3:
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
    return total

def do_maths(equation):
    print("Equation:", equation)
    active_equation = []
    bracketed_expression = []

    # check for brackets, maths them first and keep a number and operator
    inBracket = False
    for element in equation:
        print(element)

        if '(' in element and not inBracket: #wong
            inBracket = True
            bracketed_expression.append(element[1:])
        elif ')' in element:
            inBracket = False
            bracketed_expression.append(element[0:-1])
            active_equation.append(do_maths(bracketed_expression))
            bracketed_expression.clear()
        elif (inBracket):
            bracketed_expression.append(element)
        else:
            active_equation.append(element)

        print("Active:", active_equation, "Bracketed:", bracketed_expression)
    print("End EQ:", active_equation)

    total = left_right_maths(bracketed_expression if (len(active_equation) == 0) else active_equation)

    print("Total:", total)
    return str(total) # to keep it all consistent

f = open("input.txt", "r")
infile = f.read().splitlines()
f.close()

sum = 0
for equation in infile:
    equation = equation.split(' ')
    sum += int(do_maths(equation))
print("End sum:", sum)
