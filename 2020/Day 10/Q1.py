def find_difference(num1, num2):
    #print(num1, num2, "difference", num2-num1)
    return num2-num1

f = open("example1.txt", "r")
infile = f.read().splitlines()
f.close()

# build array
sorted_array = []
for item in infile:
    sorted_array.append(int(item))
sorted_array.sort()

print("Values:", sorted_array)

# use dictionary to store joltage numbers starting at 0 and ending at max + 3
differences = {1:0, 2:0, 3:0}
differences[find_difference(0, sorted_array[0])] += 1
differences[3] += 1

for i in range(len(sorted_array)):
    if (i + 1) == len(sorted_array):
        break
    difference = find_difference(sorted_array[i], sorted_array[i+1])
    differences[difference] += 1

print(differences)
print(70*30)
