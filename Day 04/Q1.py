def build_dict(passport):
    dict_entry = {}
    # Make key:value pairs and return dictionary of them for the given passport
    for i in range(len(passport)):
        dict_entry[passport[i][0:3]] = passport[i][4::]
    return dict_entry

def check_list(list, entry):
    for field in list:
        if field not in entry.keys():
            return False
    return True

f = open("input.txt", "r")
infile = f.read().split("\n\n")
f.close()

# Build dictionary of all passports
passports = {}
for entry in range(len(infile)):
    line = infile[entry].replace("\n", " ").split()
    passports[entry] = build_dict(line)

# Check each passport has all expected fields
valid_count = 0
expected_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
for key in passports.keys():
    passport = passports[key]

    # If every expected field is in the passport
    if check_list(expected_fields, passport):
        valid_count += 1

print(valid_count)
