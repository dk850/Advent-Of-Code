import sys

# parse and read in the map of risk values
f = open("testlist.txt", "r")
input = f.read().splitlines()
risk_map = [list(int(x) for x in x) for x in input]  # split the strings into individual elements

for i in risk_map:
    print(i)
