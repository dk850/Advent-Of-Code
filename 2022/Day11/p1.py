f = open("example", "r")
input = f.read().splitlines()


# Hold money business in a class
monkeys = {}
class Monkey:
    def __init__(self):
        self.items = []
        self.operation = "*-1"
        self.test = -1
        self.ifTrue = -1
        self.ifFalse = -1

    def addItem(self, newItem):
        self.items.append(newItem)
    
    def setOperation(self, newOperation):
        self.operation = str(newOperation)
    
    def setTest(self, newTest):
        self.test = newTest
    
    def setTrue(self, newTrue):
        self.ifTrue = newTrue
    def setFalse(self, newFalse):
        self.ifFalse = newFalse

    def operate(self, old):
        return print("old self.operation")
    
    def __str__(self):
        return f"Items: {self.items}\n"\
                f"Operation: old{self.operation}\n"\
                f"Test: item divisible by {self.test}\n"\
                f"If test is true: throw to monkey {self.ifTrue}\n"\
                f"If test is false: throw to monkey {self.ifFalse}"


# parse monkeys
active_monkey = -1
for line in input:
    # build new monkey
    if line[0:6] == "Monkey":
        line = line.split(' ')
        line[1] = line[1][:-1]
        monkeys[line[1]] = Monkey()
        active_monkey = line[1]

    # add items
    elif "Starting items:" in line:
        line = line.split(': ')
        items = line[1].split(', ')
        for item in items:
            monkeys[active_monkey].addItem(item)
    
    # add operation as string
    elif "Operation:" in line:
        line = line.split(': ')
        operation = line[1].split(' ')
        operation = str(operation[-2])+str(operation[-1])
        monkeys[active_monkey].setOperation(operation)
    
    # add test as int to divide by
    elif "Test:" in line:
        line = line.strip("Test: ")
        line = line.split(" by ")
        monkeys[active_monkey].setTest(line[1])

    # add true outcome
    elif "If true:" in line:
        line = line.split('to monkey ')
        monkeys[active_monkey].setTrue(line[1])

    # add false outcome
    elif "If false:" in line:
        line = line.split('to monkey ')
        monkeys[active_monkey].setFalse(line[1])

    # print built monkey
    if line == "":
        print(active_monkey+":", monkeys[active_monkey])
        print()

# run rounds