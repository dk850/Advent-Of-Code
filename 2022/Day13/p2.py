f = open("input", "r")
input = f.read().splitlines()
correctPairIndicies = []  # final output array


def isListSmaller(l1, l2):  # True = left side smaller. False = right side smaller
    global correctPairIndicies, pairIndex
    #print("COMPARE:", l1, l2)

    # check for nested lists
    for index in range(len(l1)):
        if index == len(l2):  # right side ran out of items
            #print("Right side ran out")
            return False
        #print("CP:", l1[index], l2[index])

        if isinstance(l1[index], list):  # if element is list, recurse
            # if list is only 1 element of type int, try to compare
            if len(l1[index]) == 1 and isinstance(l1[index][0], int):
                #print("1Convert", l1[index], "to", l1[index][0])
                l1[index] = l1[index][0]
            else:
                if not isinstance(l2[index], list):
                    l2[index] = [ l2[index] ]
                out = isListSmaller(l1[index], l2[index])
                if out == True:
                    return True
                if out == False:
                    return False
                continue

        if isinstance(l2[index], list):  # if element is list, recurse
            # if list is only 1 element, try to compare
            if len(l2[index]) == 1 and isinstance(l2[index][0], int):
                #print("2Convert", l2[index], "to", l2[index][0])
                l2[index] = l2[index][0]
            else:
                if not isinstance(l1[index], list):
                    l1[index] = [ l1[index] ]
                out = isListSmaller(l1[index], l2[index])
                if out == True:
                    return True
                if out == False:
                    return False
                continue
        
        #print("  CP:", l1[index], l2[index])
        if l1[index] < l2[index]:
            #print("Items in right order")
            return True  # true if L<R
        elif l1[index] > l2[index]:
            #print("Items in wrong order")
            return False  # false if L>R  ;  else continue

    if len(l1) < len(l2):
        #print("Left side ran out")
        return True
    #print("BOTTOM")
    return -1


def bubbleSortAOC(array):
    n = len(array)

    for i in range(n):
        sorted = True

        for j in range(n - i - 1):
            if not isListSmaller(array[j], array[j+1]):  # has to be not for inverse of our sort
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False

        if sorted:
            break

    return array


# build array
array = []
for item in input:
    if item == "":
        continue
    else:
        array.append(eval(item))

for i in array:
    print(i)
print()

sortedArray = bubbleSortAOC(array)
indicies = []
for i in sortedArray:
    print(i)

# get answer by copying output into text editor, search for the [2] and [6]
# cant just print the index due to how the sort changes the input
# will look something like [[[[[2]]]]] and [[[[6]]]]