class Region:
    def __init__(self, id, letter): 
        self.id = id
        self.letter = letter
        self.perimeter = 0
        self.area = 0

input_map = []
fstream = open("input.txt", 'r')
line = fstream.readline()

all_regions = []
coordinates_to_region = {}

while line:
    input_map.append(line.strip())
    line = fstream.readline()

# Flood fill to find the entire region
def create_region(x, y, input_map, coordinates_to_region, all_regions):
    region_id = len(coordinates_to_region) + 1
    region_letter = input_map[y][x]
    new_region = Region(region_id, region_letter)
    all_regions.append(new_region)
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if (x, y) in coordinates_to_region:
            continue
        new_region.area += 1
        coordinates_to_region[(x, y)] = new_region
        # Check all four directions
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(input_map[0]) and 0 <= new_y < len(input_map) and input_map[new_y][new_x] == region_letter:
                stack.append((new_x, new_y))
            else:
                new_region.perimeter += 1 #we are at the edge of the region

# Walk the map. For every cell, if it's not in a region, flood fill a new region starting there 
for y in range(len(input_map)):
    for x in range(len(input_map[y])):
        if (x, y) not in coordinates_to_region.keys():
            # This is a new region
            create_region(x, y, input_map, coordinates_to_region, all_regions)
        #else do nothing

running_total = 0
for region in all_regions:
    print(region.id, region.letter, region.area, region.perimeter)
    running_total += region.area * region.perimeter

print(running_total)