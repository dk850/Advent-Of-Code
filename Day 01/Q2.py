import time

f = open("values.txt", "r")
mylist = f.read().splitlines()

for i in mylist:
    for j in mylist:
        for k in mylist:
            if (int(i)+int(j)+int(k)) == 2020:
                print(int(i)*int(j)*int(k))

# Could sort list, add top and tails to see if > or < than 2020, half it, etc
# should read the lines as integers rather than parsing every string as int
# This is inneficient but works I guess
