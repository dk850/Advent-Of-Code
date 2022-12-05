import string
priorities = dict()
for index, letter in enumerate(string.ascii_lowercase):
	priorities[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
	priorities[letter] = index + 27

f = open("input", "r")
input = f.read().splitlines()

letters=[]
for i in range(int(len(input)/3)):
	print(input[i*3])

	for letter in input[(i*3)]:
		if letter in input[(i*3)+1] and letter in input[(i*3)+2]:
			print(letter, "in 3 elves")
			letters.append(letter)
			break

sum=0
for letter in letters:
	sum+=priorities[letter]

print(sum)
