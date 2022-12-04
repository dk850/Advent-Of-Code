import string
priorities = dict()
for index, letter in enumerate(string.ascii_lowercase):
	priorities[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
	priorities[letter] = index + 27

f = open("input", "r")
input = f.read().splitlines()

letters=[]
for line in input:
	splitat=int(len(line)/2)
	left, right = line[:splitat], line[splitat:]

	for letter in left:
		if letter in right:
			print(letter)
			dbl_letter=letter
			break

	letters.append(dbl_letter)

print(letters)

sum=0
for letter in letters:
	sum+=priorities[letter]

print(sum)
