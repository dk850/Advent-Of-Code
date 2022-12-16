f = open("example", "r")
input = f.read().splitlines()
#input = [x.split(',') for x in input ]  # split input on , to separate it easier

for l in input:
    print(l)