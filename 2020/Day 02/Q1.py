def check_pol(policy, password):
    # Parse Policy
    pos=0
    for number in policy:
        if number == "-":
            PolMin = int(policy[0:pos])
            breakpoint=pos
        if number == " ":
            PolMax = int(policy[breakpoint+1:pos])
            PolLetter = policy[pos+1]
            break
        pos+=1

    # Check if Password fits the parsed Policy
    PCount = password.count(PolLetter)
    if( (PCount < PolMin) | (PCount > PolMax) ):
        return False
    else:
        return True

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
