fstream = open("input.txt", 'r')

# return 1 if the grid going in the chosen direction reads XMAS, 0 otherwise
def tryDirection(x, y, xDelta, yDelta, lines):

    #first, retun 0 if we are going to walk off the edge
    if x + 3 * xDelta >= len(lines[y]) or x + 3 * xDelta < 0:
        return 0
    if y + 3 * yDelta >= len(lines) or y + 3 * yDelta < 0:
        return 0
    targets = ['X', 'M', 'A', 'S']
    for i in range(0, 4):
        if lines[y + i * yDelta][x + i * xDelta] != targets[i]:
            return 0
    return 1

def tryAllDirections(x, y, lines):
    total = 0
    for xDelta in [-1, 0, 1]:
        for yDelta in [-1, 0, 1]:
            if xDelta == 0 and yDelta == 0:
                continue
            total += tryDirection(x, y, xDelta, yDelta, lines)
    return total

runningTotal = 0
lines = []
line = fstream.readline()
while line:
    lines.append(line)
    line = fstream.readline()

for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        runningTotal += tryAllDirections(x, y, lines)

print(runningTotal)
