f = open("input", "r")
input = f.read().splitlines()[0]
print(input)

pos=0
while True:  # p2 = increase pos vars from 4 -> 14. decently efficient looping makes this complete in ~0.1s
    found = False
    if pos+14 > len(input):
        print("pos:", pos, "input len:", len(input))
        break
    substr=input[pos:pos+14]
    #print(substr)

    pos_increase=0
    for letter in substr:
        if substr.count(letter) > 1:
            pos_increase+=(substr.find(letter)+1)  # increase position by where duplicate letter found
            break
    if pos_increase == 0:
        found=True
    else:
        pos+=pos_increase

    if found:
        print(pos+14)
        break
