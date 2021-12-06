# read in the fish timers
f = open("input1.txt", "r")
fish_list = f.read().split(',')
fish_list = [int(x.strip()) for x in fish_list]

DAYS_TO_AGE = 256
fish_ages = {}  # dict of {age : amount of fish with age}
for day in range(DAYS_TO_AGE+1):
    print("Calculating Day:", day)

    # initial population of dict
    if day == 0:

        # build dict
        fish_ages[0] = 0
        fish_ages[1] = 0
        fish_ages[2] = 0
        fish_ages[3] = 0
        fish_ages[4] = 0
        fish_ages[5] = 0
        fish_ages[6] = 0
        fish_ages[7] = 0
        fish_ages[8] = 0

        # populate dict with current fish timers
        for fish in fish_list:
            fish_ages[fish] += 1


    # for every other day
    else:
        reset_new_fish = 0  # counter to hold how many fish are to be spawned
        for i in range(9):

            if i == 0:  # 0 is special case as we need to reset the timer and add new fish
                reset_new_fish = fish_ages[i]  # put this value in a variable as they cannot age on the first day as this counts as the age so we must do this at the end
            else:
                fish_ages[i-1] = fish_ages[i]  # move all fish from this age to the age below
                fish_ages[i] = 0  # then set this to 0, this is okay as we start from the bottom age and go up

        # day has passed so insert the fish that have spawned new ones back to age 6 and 8 for the spawned fish so we dont spawn and age them on the same day
        fish_ages[8] = reset_new_fish
        fish_ages[6] += reset_new_fish


# get answer
sum = 0
for key in fish_ages:
    sum += fish_ages[key]
print(sum)

# NOTE : Needed a new implementation for part 2 to avoid the exponential growth - we keep track of the NUMBER rather than the actual fish themselves as we did in p1 - took longer but is neccesary
