fstream = open("input.txt", 'r')
line = fstream.readline()

class Map:
    def __init__(self):
        self.walls = set()
        self.crates = set()
        self.fish = (0, 0)

y = 0
phase = 1
commands = ""
map = Map()
while line:
    # a blank line separates the two phases
    if len(line) <= 1:
        phase = 2
        line = fstream.readline()
        continue
    if phase == 1:
        for x in range(len(line)):
            if line[x] == "#":
                map.walls.add((x, y))
            elif line[x] == "O":
                map.crates.add((x, y))
            elif line[x] == "@":
                map.fish = (x, y)
        y += 1
    else:
        commands += line.strip()
    line = fstream.readline()

def print_map(map):
    for y in range(8):
        for x in range(8):
            if (x, y) in map.walls:
                print("#", end="")
            elif (x, y) in map.crates:
                print("O", end="")
            elif (x, y) == map.fish:
                print("@", end="")
            else:
                print(".", end="")
        print()

def move(map, movement):
    (dx, dy) = movement
    # First, check the chosen direction to see if we hit a wall or an open space first.
    # If a wall, do nothing.
    searching = True
    (search_x, search_y) = map.fish
    while searching:
        search_x += dx
        search_y += dy
        if (search_x, search_y) in map.walls:
            return # Do nothing; we hit a wall
        if (search_x, search_y) not in map.crates:
            searching = False # We can push to an open space
        # Otherwise, this is a crate, keep going to see what's behind it
    # Now, we know we can push the crate.
    map.fish = (map.fish[0] + dx, map.fish[1] + dy)
    # If there was a crate there, move it to the empty spot we found
    # This is the same as pushing every crate, but they're all the same
    if map.fish in map.crates:
        map.crates.remove((map.fish))
        map.crates.add((search_x, search_y))

command_to_movement = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

i = 0
for command in commands:
    print_map(map)
    i += 1
    print(str(i) + " " + command)
    move(map, command_to_movement[command])

running_total = 0
for crate in map.crates:
    running_total += crate[0] + 100 * crate[1]

print(running_total)