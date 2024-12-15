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
ITERATIONS = 100

quadrants = [0, 0, 0, 0]
for bot in bots:
    print(bot)

    bot.x = (bot.x + bot.dx * ITERATIONS) % ARENA_WIDTH
    bot.y = (bot.y + bot.dy * ITERATIONS) % ARENA_HEIGHT
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
    
print(len(bots))
print(quadrants)
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
