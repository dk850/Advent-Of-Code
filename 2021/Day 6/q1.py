# read in the fish timers
f = open("input1.txt", "r")
fish_list = f.read().split(',')
fish_list = [int(x.strip()) for x in fish_list]

DAYS_TO_AGE = 80
for day in range(DAYS_TO_AGE+1):
    print("Calculating Day:", day)
    if day != 0:

        for fish_pos in range(len(fish_list)):

            if fish_list[fish_pos] == 0:  # time for a new fish, spawn a new one and reset timer
                fish_list[fish_pos] = 6
                fish_list.append(8)

            else:  # age fish
                fish_list[fish_pos] -= 1

print(len(fish_list))
