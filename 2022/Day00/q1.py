f = open("input1.txt", "r")
input = f.read().splitlines()
input = [x.split(',') for x in input ]  # split input on , to separate it easier
