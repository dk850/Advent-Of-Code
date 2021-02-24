# Check how many different letters are in the group by removing letters
# from the alphabet if present and then checking the size difference
def check_letters(group):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", \
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabet_size = len(alphabet)

    for person in group:
        for letter in person:
            if letter in alphabet:
                alphabet.remove(letter)
    questions_asked = alphabet_size - len(alphabet)

    return questions_asked

f = open("input.txt", "r")
infile = f.read().split("\n\n")
f.close()

count = 0
for entry in range(len(infile)):
    group = infile[entry].replace("\n", " ").split()
    #print(group)

    count += check_letters(group)
print(count)
