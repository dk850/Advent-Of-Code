def validate_entry(passport):
    expected_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    optional_fields = ("cid")
    expected_count = 0
    optional_count = 0

    # If the passport is smaller than expected fields then it cant contain all expected fields
    if len(passport) < len(expected_fields):
        #print("Too small")
        return False

    # If the passport is the maximum size then it must contain all expected and all optional fields
    elif len(passport) == (len(expected_fields) + len(optional_fields[0])):
        #print("Maximum size")
        return True

    # If the passport length is not maximum we need to check it still has all expected fields
    else:
        # Check all expected fields are there
        for entry in passport:
            for field in expected_fields:
                #print("Checkfor:", field)
                if field == entry[0:3]:
                    #print("Found expected", field)
                    expected_count += 1
                    break
        #print("Expected Count:", expected_count)

        # If all expected fields are there then it is valid
        if expected_count == len(expected_fields):
            return True
        else:
            return False

f = open("input.txt", "r")
infile = f.read().split("\n\n")
f.close()

batch = []
for index in range(len(infile)):
    if "\n" in infile[index]:
        batch.append(infile[index].replace("\n", " ").split(" "))
#print(len(batch))

valid_count = 0
for passport in batch:
    #print(passport)
    if(validate_entry(passport)):
        valid_count += 1
        #print("Valid:", passport)
    else:
        1+1
        #print("Failed:", passport)

print("Total Count:", valid_count)
