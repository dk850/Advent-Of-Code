f = open("input1", "r")
input = f.read().splitlines()

elves = {}
elf = 0
total = 0
for entry in input:
    if entry == "":
        elves[elf] = total
        elf += 1
        total = 0
    else:
        total += int(entry)

print(elves)
print()
print(sorted(elves.items(), key=lambda item: item[1]))
