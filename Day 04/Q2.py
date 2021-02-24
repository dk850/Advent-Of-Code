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

def check_valid_list(field_list, entry):
    valid_count = 0

    for field in field_list:
        if field == "byr":
            #print("byr Value:", entry[field])
            if( (int(entry[field]) < 1920) | (int(entry[field]) > 2002) ):
                return False

        elif field == "iyr":
            #print("iyr Value:", entry[field])
            if( (int(entry[field]) < 2010) | (int(entry[field]) > 2020) ):
                return False

        elif field == "eyr":
            #print("eyr Value:", entry[field])
            if( (int(entry[field]) < 2020) | (int(entry[field]) > 2030) ):
                return False

        elif field == "hgt":
            #print("hgt Value:", entry[field])
            if entry[field][-2:] == "cm":
                if( (int(entry[field][0:-2]) < 150) | (int(entry[field][0:-2]) > 193) ):
                    return False
            elif entry[field][-2:] == "in":
                if( (int(entry[field][0:-2]) < 59) | (int(entry[field][0:-2]) > 76) ):
                    return False
            else:
                return False

        elif field == "hcl":
            #print("hcl Value:", entry[field])
            valid_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", \
                            "a", "b", "c", "d", "e", "f"]

            if entry[field][0] != "#":
                return False
            if len(entry[field]) > 7:
                return False
            try:
                for val in range(1,7):
                    if entry[field][val] not in valid_chars:
                        return False
            except:
                return False

        elif field == "ecl":
            #print("ecl Value:", entry[field])
            valid_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

            if len(entry[field]) > 3:
                return False
            if entry[field] not in valid_list:
                return False

        elif field == "pid":
            #print("pid Value:", entry[field])
            valid_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

            if len(entry[field]) > 9:
                return False
            try:
                for val in range(0,9):
                    if entry[field][val] not in valid_chars:
                        return False
            except:
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

    # If every expected field is in the passport, check they contain correct data
    if check_list(expected_fields, passport):
        if check_valid_list(expected_fields, passport):
            valid_count += 1

print(valid_count)
