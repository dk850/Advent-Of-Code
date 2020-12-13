# Check how many different letters are in the group by removing letters
# from the alphabet if present and then checking the size difference
def check_letters(group):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", \
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    found_letters = []
    alphabet_size = len(alphabet)

    # For groups with only one person
    if int(len(group)) == 1:
        for letter in group[0]:
            if letter in alphabet:
                alphabet.remove(letter)
        questions_asked = alphabet_size - len(alphabet)
        return questions_asked

    # If multiple people in group we keep a list of letters each person has said
    for person in group:
        for letter in person:
            found_letters.append(letter)

    # If a letter is in the list the same amount of times as people, everyone has said it
    questions_asked = 0
    for letter in alphabet:
        if found_letters.count(letter) == len(group):
            questions_asked += 1
    return questions_asked

f = open("input.txt", "r")
infile = f.read().split("\n\n")
f.close()

count = 0
for entry in range(len(infile)):
    group = infile[entry].replace("\n", " ").split()
    count += check_letters(group)
print(count)
