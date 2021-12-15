f1 = open("lst1.txt", "r")
f2 = open("lst2.txt", "r")

l1 = f1.read().splitlines()
l2 = f2.read().splitlines()

if abs(len(l1) - len(l2)) != 0:
    print("Difference of", abs(len(l1) - len(l2)))

    if len(l1) > len(l2):
        print("l1 longer")
    else:
        print("l2 longer")

missing = []
for i in range(len(l1 if len(l1) > len(l2) else l2)):
    if l1[i] not in l2:
        missing.append(l1[i])
    else:
        print(l1[i], "in l1 and l2")

print("Missing:", missing)
