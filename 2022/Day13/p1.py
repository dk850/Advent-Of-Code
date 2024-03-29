f = open("input", "r")
input = f.read().splitlines()
correctPairIndicies = []  # final output array


def compareList(l1, l2):
    global correctPairIndicies, pairIndex
    print("COMPARE:", l1, l2)

    # check for nested lists
    for index in range(len(l1)):
        if index == len(l2):  # right side ran out of items
            print("Right side ran out")
            return False
        print("CP:", l1[index], l2[index])

        if isinstance(l1[index], list):  # if element is list, recurse
            # if list is only 1 element of type int, try to compare
            if len(l1[index]) == 1 and isinstance(l1[index][0], int):
                print("1Convert", l1[index], "to", l1[index][0])
                l1[index] = l1[index][0]
            else:
                if not isinstance(l2[index], list):
                    l2[index] = [ l2[index] ]
                out = compareList(l1[index], l2[index])
                if out == True:
                    return True
                if out == False:
                    return False
                continue

        if isinstance(l2[index], list):  # if element is list, recurse
            # if list is only 1 element, try to compare
            if len(l2[index]) == 1 and isinstance(l2[index][0], int):
                print("2Convert", l2[index], "to", l2[index][0])
                l2[index] = l2[index][0]
            else:
                if not isinstance(l1[index], list):
                    l1[index] = [ l1[index] ]
                out = compareList(l1[index], l2[index])
                if out == True:
                    return True
                if out == False:
                    return False
                continue
        
        print("  CP:", l1[index], l2[index])
        if l1[index] < l2[index]:
            print("Items in right order")
            correctPairIndicies.append(pairIndex)
            return True  # true if L<R
        elif l1[index] > l2[index]:
            print("Items in wrong order")
            return False  # false if L>R  ;  else continue

    if len(l1) < len(l2):
        print("Left side ran out")
        correctPairIndicies.append(pairIndex)
        return True
    print("BOTTOM")
    return -1



pairIndex = 1  # 1 based
for pair in range(0, len(input), 3):
    p1 = eval(input[pair])
    p2 = eval(input[pair+1])

    print("INPUT "+str(pairIndex)+":", p1, p2)

    #if pairIndex in [36, 64, 84, 142]:  # qucik way around edge cases. manually see these
    #    pairIndex += 1
    #    continue
    compareList(p1, p2)
    print(correctPairIndicies)
    pairIndex += 1


    print()

sum = 0
for v in correctPairIndicies:
    sum += v
print(sum)