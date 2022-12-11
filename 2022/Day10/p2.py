f = open("input", "r")
input = f.read().splitlines()
input = [x.split(' ') for x in input ]  # split input on , to separate it easier

clock = 0
x_reg = 1
monitor_clock = [40, 80, 120, 160, 200, 240]  # times we need signal strength
o_str = ""
p_pos = 0


# to draw either a . or # 
def draw_sprite():
    global o_str, p_pos

    # get sprite positions
    s_pos = [x_reg-1, x_reg, x_reg+1]  # sprite is 3 wide depending on whats in the x register
    if p_pos in s_pos:
        o_str += "#"
    else:
        o_str += "."
    
    p_pos += 1
    if p_pos % 40 == 0:  # start newline to simulate new row
        o_str += "\n"
        p_pos = 0


for line in input:
    draw_sprite()  # draw our sprite on the line

    # calculate instruction
    if line[0] == "noop":
        clock += 1
    elif line[0] == "addx":
        clock += 1
        draw_sprite()  # addx takes 2 clocks so need to re-draw
    
    if line[0] == "addx":  # 2 clocks, add to reg on 2nd clock. Sprite drawn at start of loop
        x_reg += int(line[1])
        clock += 1

print(o_str)