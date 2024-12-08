from enum import Enum

class Direction(Enum):
    NORTH = 1,
    EAST = 2,
    SOUTH = 3,
    WEST = 4


fstream = open("input.txt", 'r')
map = []
line = fstream.readline()
currentLine = 0
while line:
    map += [line.strip()]
    seek = line.find("^")
    if seek >= 0:
        (guardX, guardY) = (seek, currentLine)

    currentLine += 1
    line = fstream.readline()
print(guardX, guardY)

def march():
    global guardX
    global guardY
    global currentDirection
    if currentDirection == Direction.NORTH:
        if guardY == 0:
            return False
        if map[guardY - 1][guardX] == "#":
            currentDirection = Direction.EAST
        else:
            guardY -= 1
    elif currentDirection == Direction.EAST:
        if guardX == len(map[0]) - 1:
            return False
        if map[guardY][guardX + 1] == "#":
            currentDirection = Direction.SOUTH
        else:
            guardX += 1
    elif currentDirection == Direction.SOUTH:
        if guardY == len(map) - 1:
            return False
        if map[guardY + 1][guardX] == "#":
            currentDirection = Direction.WEST
        else:
            guardY += 1
    else:
        if guardX == 0:
            return False
        if map[guardY][guardX - 1] == "#":
            currentDirection = Direction.NORTH
        else:
            guardX -= 1

    return True

visitedLocations = {}
currentDirection = Direction.NORTH
stillOnMap = True
while stillOnMap:
    if (guardX, guardY) not in visitedLocations:
        visitedLocations[(guardX, guardY)] = 0
    visitedLocations[(guardX, guardY)] += 1
    stillOnMap = march()

print (len(visitedLocations))
