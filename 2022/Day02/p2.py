f = open("input1", "r")
input = f.read().splitlines()
input = [x.split(' ') for x in input ]  # split input on , to separate it easier

# A = rock, B = paper, C = scissors
#      1  ,       2  ,         3
#  X,0 = loss ,  Y,3= draw   ,  Z,6 = win

#print(input)

bigScore=0
for round in input:
    score=0
    match round[0]:
        case "A":
            match round[1]:
                case "X":
                    score=(3 + 0)
                case "Y":
                    score=(1 + 3)
                case "Z":
                    score=(2 + 6)

        case "B":
            match round[1]:
                case "X":
                    score=(1 + 0)
                case "Y":
                    score=(2 + 3)
                case "Z":
                    score=(3 + 6)

        case "C":
            match round[1]:
                case "X":
                    score=(2 + 0)
                case "Y":
                    score=(3 + 3)
                case "Z":
                    score=(1 + 6)
    bigScore+=score
print(bigScore)
