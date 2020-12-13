import time

f = open("values.txt", "r")
mylist = f.read().splitlines()

for i in mylist:
    for j in mylist:
        if (int(i)+int(j)) == 2020:
            print(int(i)*int(j))

# Could sort list, add top and tails to see if > or < than 2020, half it, etc
# should read the lines as integers rather than parsing every string as int
