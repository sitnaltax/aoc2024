from enum import Enum

class Direction(Enum):
    NORTH = 1,
    EAST = 2,
    SOUTH = 3,
    WEST = 4

class Guard:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

fstream = open("input.txt", 'r')
map = []
line = fstream.readline()
currentLine = 0

while line:
    map += [line.strip()]
    seek = line.find("^")
    if seek >= 0:
        (startingGuardX, startingGuardY) = (seek, currentLine)

    currentLine += 1
    line = fstream.readline()

def march(guard):
    if guard.direction == Direction.NORTH:
        if guard.y == 0:
            return False
        if map[guard.y - 1][guard.x] == "#":
            guard.direction = Direction.EAST
        else:
            guard.y -= 1
    elif guard.direction == Direction.EAST:
        if guard.x == len(map[0]) - 1:
            return False
        if map[guard.y][guard.x + 1] == "#":
            guard.direction = Direction.SOUTH
        else:
            guard.x += 1
    elif guard.direction == Direction.SOUTH:
        if guard.y == len(map) - 1:
            return False
        if map[guard.y + 1][guard.x] == "#":
            guard.direction = Direction.WEST
        else:
            guard.y += 1
    else:
        if guard.x == 0:
            return False
        if map[guard.y][guard.x - 1] == "#":
            guard.direction = Direction.NORTH
        else:
            guard.x -= 1
    return True

visitedLocations = {}
stillOnMap = True
guard = Guard(startingGuardX, startingGuardY, Direction.NORTH)
while stillOnMap:
    if (guard.x, guard.y) not in visitedLocations:
        visitedLocations[(guard.x, guard.y)] = 0
    visitedLocations[(guard.x, guard.y)] += 1
    stillOnMap = march(guard)

print (len(visitedLocations))

# For each position, put an obstacle there. See if the guard leaves or enters a loop.
loopsFound = 0
for position in visitedLocations.keys():
    if position == (startingGuardX, startingGuardY):
        continue
    map[position[1]] = map[position[1]][:position[0]] + "#" + map[position[1]][position[0] + 1:]
    visitedLocationsInTrial = {}
    stillOnMap = True
    guard = Guard(startingGuardX, startingGuardY, Direction.NORTH)
    while stillOnMap:
        if (guard.x, guard.y) not in visitedLocationsInTrial:
            visitedLocationsInTrial[(guard.x, guard.y)] = 0
        visitedLocationsInTrial[(guard.x, guard.y)] += 1
        if visitedLocationsInTrial[(guard.x, guard.y)] > 4:
            loopsFound += 1
            # put the map back to how it was
            map[position[1]] = map[position[1]][:position[0]] + "." + map[position[1]][position[0] + 1:]
            break
        stillOnMap = march(guard)

    # we fell off the map. No loop in this one. put the map back to how it was
    map[position[1]] = map[position[1]][:position[0]] + "." + map[position[1]][position[0] + 1:]

print(loopsFound)