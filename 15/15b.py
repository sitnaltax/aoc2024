fstream = open("input.txt", 'r')
line = fstream.readline()

class Map:
    def __init__(self):
        self.walls = set()
        self.crates = set()
        # A crate is uniquely identified by its left half, but we track the right half for convenience
        self.crate_right_halves = set()
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
                map.walls.add((2 * x, y))
                map.walls.add((2 * x + 1, y))
            elif line[x] == "O":
                map.crates.add((2 * x, y))
                map.crate_right_halves.add((2 * x + 1, y))
            elif line[x] == "@":
                map.fish = (2 * x, y)
        y += 1
    else:
        commands += line.strip()
    line = fstream.readline()

def print_map(map):
    for y in range(10):
        for x in range(20):
            if (x, y) in map.walls:
                print("#", end="")
            elif (x, y) in map.crates:
                print("[", end="")
            elif (x, y) in map.crate_right_halves:
                print("]", end="")                
            elif (x, y) == map.fish:
                print("@", end="")
            else:
                print(".", end="")
        print()

def contains_crate(map, x, y):
    return (x, y) in map.crates or (x, y) in map.crate_right_halves

def move(map, movement):
    (dx, dy) = movement
    # First, check the chosen direction to see if we hit a wall or an open space first.
    # If a wall, do nothing.
    spaces_to_check = [map.fish]
    # If we are pushing north or south, this will be much more complicated, because
    # each crate can push two other crates, and we will need to check and then move all of them
    crates_to_move = set()
    while len(spaces_to_check) > 0:
        next_spaces_to_check = []
        for (search_x, search_y) in spaces_to_check:
            search_x += dx
            search_y += dy
            if (search_x, search_y) in map.walls:
                return # Do nothing; we hit a wall
            if contains_crate(map, search_x, search_y):
                if dy == 0: #we're pushing from the left or right
                    if dx == 1: #we're pushing from the left
                        crates_to_move.add((search_x, search_y))
                        next_spaces_to_check.append((search_x + dx, search_y))
                    else: #we're pushing from the right
                        crates_to_move.add((search_x - 1, search_y))
                        next_spaces_to_check.append((search_x + dx, search_y))
                else: #we're pushing from the top or bottom
                    if (search_x, search_y) in map.crates:
                        crates_to_move.add((search_x, search_y))
                        next_spaces_to_check.append((search_x, search_y))
                        next_spaces_to_check.append((search_x + 1, search_y))
                    else: #we're pushing the right half
                        crates_to_move.add((search_x - 1, search_y))
                        next_spaces_to_check.append((search_x - 1, search_y))
                        next_spaces_to_check.append((search_x, search_y))
        spaces_to_check = next_spaces_to_check
    # Now, we know we can push the crate.
    map.fish = (map.fish[0] + dx, map.fish[1] + dy)
    # If there was a crate there, move it to the empty spot we found
    # This is the same as pushing every crate, but they're all the same
    print(crates_to_move)
    # Because we're using a set, have to remove all of them first and then add the new ones
    for crate in crates_to_move:
        map.crates.remove(crate)
        map.crate_right_halves.remove((crate[0] + 1, crate[1]))
    for crate in crates_to_move:
        map.crates.add((crate[0] + dx, crate[1] + dy))
        map.crate_right_halves.add((crate[0] + dx + 1, crate[1] + dy))

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