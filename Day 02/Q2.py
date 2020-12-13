def check_pol(policy, password):
    # Parse Policy
    pos=0
    for number in policy:
        if number == "-":
            PolPos1 = int(policy[0:pos])
            breakpoint=pos
        if number == " ":
            PolPos2 = int(policy[breakpoint+1:pos])
            PolLetter = policy[pos+1]
            break
        pos+=1

    # Check if Password fits the parsed Policy
    if( (password[PolPos1-1] == PolLetter) | (password[PolPos2-1] == PolLetter) ):
        if( (password[PolPos1-1] == PolLetter) & (password[PolPos2-1] == PolLetter) ):
            return False
        else:
            return True
    else:
        return False

f = open("input.txt", "r")
pwords = f.read().splitlines()
validPwords = 0

for line in pwords:
    pos=0
    for letter in line:
        if letter == ":":
            policy = line[0:pos]
            password = line[pos+2::]
            break
        else:
            pos+=1

    if(check_pol(policy, password)):
        validPwords += 1

print("Valid Count:", validPwords)
