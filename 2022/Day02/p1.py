f = open("input1", "r")
input = f.read().splitlines()
input = [x.split(' ') for x in input ]  # split input on , to separate it easier

# A,X = rock, B,Y = paper, C,Z = scissors
#        1  ,          2  ,          3
#  0 = loss ,  3 = draw   ,  6 = win

#print(input)

bigScore=0
for round in input:
    score=0
    match round[0]:
        case "A":
            match round[1]:
                case "X":
                    score=(1 + 3)
                case "Y":
                    score=(2 + 6)
                case "Z":
                    score=(3 + 0)

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
                    score=(1 + 6)
                case "Y":
                    score=(2 + 0)
                case "Z":
                    score=(3 + 3)
    bigScore+=score
print(bigScore)
