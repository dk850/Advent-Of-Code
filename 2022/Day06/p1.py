f = open("input", "r")
input = f.read().splitlines()[0]
#print(input)

pos=0
while True:
    found = False
    if pos+4 > len(input):
        print("pos:", pos, "input len:", len(input))
        break
    substr=input[pos:pos+4]
    #print(substr)

    pos_increase=0
    for letter in substr:
        if substr.count(letter) > 1:
            pos_increase+=(substr.find(letter)+1)
            break
    if pos_increase == 0:
        found=True
    else:
        pos+=pos_increase

    if found:
        print(pos+4)
        break
