adapters = [7, 8, 9, 10, 11]

possibilities = {adapters[-1]: 1}
for a in reversed(adapters[:-1]):
    possibilities[a] = sum(possibilities.get(x, 0) for x in (a+1, a+2, a+3))
print(possibilities[0])
