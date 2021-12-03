# initialise variables
input = [1, 0, 18, 10, 19, 6]
numbers_spoken = {} # number : [times_spoken, last_spoken, most_recently_spoken]
turn = 1

# add starting numbers to the list
for number in input:
    numbers_spoken[number] = [1, 0, turn]
    latest_number = number

    #print("Turn:", turn, "Number spoken:", str(latest_number) + ":" + str(numbers_spoken[latest_number]))
    turn += 1

# loop until it reaches required turn count
while True:

    # try block throws an error if this is the first time adding a number to the list
    try:

        # if this is the first time the number has been spoken, say 0 this turn
        if numbers_spoken[latest_number][0] == 1:
            latest_number = 0

            # add 1 to the count of times_spoken for number 0,
            # change last_spoken to the most_recently_spoken value,
            # and then change most_recent to be this turn
            numbers_spoken[0] = [numbers_spoken[0][0] + 1, numbers_spoken[0][2], turn]

        # if the latest number has been spoken before, speak its age (this_turn - turn_spoken_last)
        elif numbers_spoken[latest_number][0] > 1:
            # set latest number to be the difference in when this current iterations number was previously spoken
            latest_number = numbers_spoken[latest_number][2] - numbers_spoken[latest_number][1]

            # add 1 to the count of times_spoken for this new number,
            # change last_spoken to the most_recently_spoken value,
            # and then change most_recent to be this turn
            numbers_spoken[latest_number] = [numbers_spoken[latest_number][0] + 1, numbers_spoken[latest_number][2], turn]

    # add new number to the dictionary
    except KeyError:
        numbers_spoken[latest_number] = [1, 0, turn]

    # shouldnt get here
    except:
        print("Died")
        exit()
        
    # find the 2020th number spoken
    if turn == 2020:
        print("Turn:", turn, "Number spoken:", str(latest_number) + ":" + str(numbers_spoken[latest_number]))
        break
    else:
        turn += 1
