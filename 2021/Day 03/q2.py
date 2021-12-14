def get_most_common(thelist, position):
    t_list = list(zip(*thelist))  # transpose the list
    zeros = t_list[position].count('0')  # count 0s in the string
    ones  = t_list[position].count('1')  # count 1s

    if zeros == ones:
        return '2'  # return 2 to signify they are the same value
    else:
        return '1' if ones > zeros else '0'


def get_rating(type, report):

    pos = 0
    while 1:  # continuous loop as we dont know the size, stop looping when we have 1 element
        # get either the most common or least common bit for the position based on the rules
        search_bit = get_most_common(report, pos)
        if type == 'CO2':  # inver if CO2
            if search_bit == '2':
                search_bit = '0'
            else:
                search_bit = '0' if search_bit == '1' else '1'
        else:  # else it is O2 - should error check here but this is fine for our purpose
            if search_bit == '2':
                search_bit = '1'


        # remove elements from the list where the position doesnt have the most common bit
        to_remove = []
        for element in report:
            if element[pos] != search_bit:
                to_remove.append(element)

        report = [x for x in report if x not in to_remove]  # re-build the list whilst removing elements

        pos += 1
        if len(report) == 1:  # if length is 1 we have found the correct value
            return report[0]  # return as string



f = open("input1.txt", "r")
mylist = f.read().splitlines()

# get strings
O2 = get_rating("O2", mylist)
CO2 = get_rating("CO2", mylist)

print(O2, CO2)

# turn into ints so we can multiply them together and therefore get the answer
O2_int = int(O2, 2)
CO2_int = int(CO2, 2)

print(O2_int * CO2_int)
