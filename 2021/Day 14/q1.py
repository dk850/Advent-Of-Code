from collections import Counter

# parse file into the polymer template and dictionary of rules
f = open("input1.txt", "r")
input = f.read().splitlines()
polymer_template = input[0]
polymer_rules = {}
for line in input[2:]:
    rule = line.split(' -> ')
    polymer_rules[rule[0]] = rule[1]


# loop for number of steps
step_count = 10  # q1 requires 10 steps
polymer = polymer_template
for step in range(step_count):
    end_polymer = ""  # variable for the final polymer so we dont edit it live

    # loop over each letter in the start polymer
    for letter in range(len(polymer)-1):  # loop size -1 so we dont try and index past the length of the list
        pair = str(polymer[letter])+str(polymer[letter+1])  # create a pair

        if pair in polymer_rules.keys():
            end_polymer += pair[0] + polymer_rules[pair]  # add the insertion to the final string

    end_polymer += polymer[-1]  # dont forget to re-add the last element
    polymer = end_polymer  # reset polymer to this final value for the next loop


# answer wants the most common element - least common
print("Polymer length:", len(polymer), "\nWith Frequencies:", Counter(polymer).most_common())
print("Most - Least:", Counter(polymer).most_common()[0][1] - Counter(polymer).most_common()[-1][1])
