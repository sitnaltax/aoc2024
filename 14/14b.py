import re

class Bot:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"Bot({self.x}, {self.y}, {self.dx}, {self.dy})"

bots = []
fstream = open("input.txt", 'r')
line = fstream.readline()


while line:
    (first, second) = line.strip().split(" ")
    (x, y) = first[2:].split(",")
    (dx, dy) = second[2:].split(",")
    bots.append(Bot(int(x), int(y), int(dx), int(dy)))
    line = fstream.readline()

ARENA_WIDTH = 101
ARENA_HEIGHT = 103
#ARENA_WIDTH = 11
#ARENA_HEIGHT = 7
ITERATIONS = 50000

def detect_run():
    for row in map:
        if row.find("#######") != -1:
            return True
    return False

def print_map(map):
    for row in map:
        print(row)

quadrants = [0, 0, 0, 0]
for i in range(ITERATIONS):
    map = ["." * ARENA_WIDTH for i in range(ARENA_HEIGHT)]
    for bot in bots:
        map[bot.y] = map[bot.y][:bot.x] + "#" + map[bot.y][bot.x + 1:]
        bot.x = (bot.x + bot.dx) % ARENA_WIDTH
        bot.y = (bot.y + bot.dy) % ARENA_HEIGHT
        arena_x_middle = (ARENA_WIDTH - 1) / 2
        arena_y_middle = (ARENA_HEIGHT - 1) / 2 # If a bot is exactly on the middle, it doesn't count toward any quadrant
        if (bot.x < arena_x_middle and bot.y < arena_y_middle):
            quadrants[0] += 1
        elif (bot.x > arena_x_middle and bot.y < arena_y_middle):
            quadrants[1] += 1
        elif (bot.x < arena_x_middle and bot.y > arena_y_middle):
            quadrants[2] += 1
        elif (bot.x > arena_x_middle and bot.y > arena_y_middle):
            quadrants[3] += 1
    if detect_run():
        print(i)
        print_map(map)
    

