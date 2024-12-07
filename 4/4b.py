fstream = open("input.txt", 'r')

# we'll do the same thing as 4a except search for an A as the target, S in the given direction, M in the opposite
# return 1 if the grid going in the chosen direction reads XMAS, 0 otherwise
def tryDirection(x, y, xDelta, yDelta, lines):

    #no worry about walking off the edge of the map since we always search a square
    targets = ['A', 'S', 'M']
    deltas = [0, 1, -1]
    for i in range(0, 3):
        if lines[y + deltas[i] * yDelta][x + deltas[i] * xDelta] != targets[i]:
            return 0
    return 1

def tryAllDirections(x, y, lines):
    total = 0
    for (xDelta, yDelta) in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        total += tryDirection(x, y, xDelta, yDelta, lines)
    if total == 2:
        return 1
    return 0

runningTotal = 0
lines = []
line = fstream.readline()
while line:
    lines.append(line)
    line = fstream.readline()

for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[y]) - 1):
        runningTotal += tryAllDirections(x, y, lines)

print(runningTotal)
