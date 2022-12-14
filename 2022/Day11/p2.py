from math import floor

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
        self.inspectionCount = 0

    def operate(self, old):  # inspect
        #print("OPERATE", old, "->", floor(eval(str(str(old)+self.operation))/3))
        self.inspectionCount += 1
        return floor(eval(str(str(old)+self.operation)))  # P2 no longer divided by 3
    
    def operateAll(self):
        for item in self.items:
            self.updateItem(item, self.operate(item))
            
    def testItem(self, item):
        #print("TEST:", item, "->", item%self.test)
        return True if item%self.test == 0 \
            else False
        
    def throwTo(self, item, target):
        #print("THROWING", item, target)
        monkeys[target].addItemStart(item)
        self.popItem(item)
            
            
    def addItemStart(self, newItem):
        self.items.insert(0, newItem)
        
    def addItemEnd(self, newItem):
        self.items.append(newItem)
        
    def updateItem(self, oldItem, newItem):
        self.items[self.items.index(oldItem)] = newItem        
    
    def popItem(self, toPop):
        self.items.remove(toPop)
    
    def setOperation(self, newOperation):
        self.operation = str(newOperation)
    
    def setTest(self, newTest):
        self.test = newTest
    
    def setTrue(self, newTrue):
        self.ifTrue = newTrue
    def setFalse(self, newFalse):
        self.ifFalse = newFalse
    
    def __str__(self):
        return f"Items: {self.items}\n" \
                f"Operation: old{self.operation}\n" \
                f"Test: item divisible by {self.test}\n" \
                f"If test is true: throw to monkey {self.ifTrue}\n" \
                f"If test is false: throw to monkey {self.ifFalse}\n" \
                f"Inspection Count: {self.inspectionCount}"


# parse monkeys
active_monkey = -1
for line in input:
    # build new monkey
    if line[0:6] == "Monkey":
        line = line.split(' ')
        line[1] = line[1][:-1]
        monkeys[int(line[1])] = Monkey()
        active_monkey = int(line[1])

    # add items
    elif "Starting items:" in line:
        line = line.split(': ')
        items = [int(x) for x in line[1].split(', ')]
        for item in items:
            monkeys[active_monkey].addItemEnd(item)
    
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
        monkeys[active_monkey].setTest(int(line[1]))

    # add true outcome
    elif "If true:" in line:
        line = line.split('to monkey ')
        monkeys[active_monkey].setTrue(int(line[1]))

    # add false outcome
    elif "If false:" in line:
        line = line.split('to monkey ')
        monkeys[active_monkey].setFalse(int(line[1]))

    # print built monkey
    if line == "":
        print(str(active_monkey)+":", monkeys[active_monkey])
        print()

# run rounds
ROUNDS = 10000
for round in range(ROUNDS):
    for turn in range(len(monkeys)):  # inspect and throw items 1 at a time
        #print()
        print("ROUND:", round, "TURN:", turn) 
        
        # If no items, end turn
        #print("Monkey", turn)
        #print("start items:", monkeys[turn].items)
        if len(monkeys[turn].items) == 0:
            continue  # next monkey
        
        ## PER ITEM
        # inspect operation on all items
        monkeys[turn].operateAll()  # inspect and divide all by 3
        items = monkeys[turn].items.copy()
        #print("updated items:", items)
        for item in items:
            #print("Instpecting:", item)
            
            # test worry level T/F
            if monkeys[turn].testItem(item):
                monkeys[turn].throwTo(item, monkeys[turn].ifTrue)
            else:
                monkeys[turn].throwTo(item, monkeys[turn].ifFalse)
                
print()
print()
mostInspections = []
for m in monkeys:
    print("Monkey", str(m)+":", monkeys[m])
    print()
# manually multiply the biggest 2 out of 8 together for p1 answer