input_map = []
fstream = open("input.txt", 'r')
line = fstream.readline()

while line:
    input_map.append(list(map(int, list(line.strip()))))
    line = fstream.readline()

# now the input_map is a list of lists of integers

trailheads = []

for i in range(len(input_map)):
    for j in range(len(input_map[i])):
        if input_map[i][j] == 0:
            trailheads.append((j, i))


def process_trailhead(trailhead, input_map):
    locations = [trailhead]
    for target_number in range(1, 10):
        new_locations = set()
        for location in locations:
            x, y = location
            if x > 0 and input_map[y][x - 1] == target_number:
                new_locations.add((x - 1, y))
            if x < len(input_map[0]) - 1 and input_map[y][x + 1] == target_number:
                new_locations.add((x + 1, y))
            if y > 0 and input_map[y - 1][x] == target_number:
                new_locations.add((x, y - 1))
            if y < len(input_map) - 1 and input_map[y + 1][x] == target_number:
                new_locations.add((x, y + 1))
        print (target_number, new_locations)
        locations = new_locations
        if len(locations) == 0:
            return 0 #we will never reach anywhere
    return len(locations) #this is how many 9's we could reach

running_total = 0
for trailhead in trailheads:
    print (trailhead)
    print (process_trailhead(trailhead, input_map))
    running_total += process_trailhead(trailhead, input_map)

print(running_total)
