class Region:
    def __init__(self, id, letter): 
        self.id = id
        self.letter = letter
        self.north_borders = []
        self.south_borders = []
        self.east_borders = []
        self.west_borders = []
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
                if dy == -1:
                    new_region.north_borders.append((x, y))
                elif dy == 1:
                    new_region.south_borders.append((x, y))
                elif dx == -1:
                    new_region.west_borders.append((x, y))
                else:
                    new_region.east_borders.append((x, y))

def calculate_sides(region):
    # For the north side:
    # First, separate the borders by their y-coordinate
    # Then, sort them by x-coordinate
    # Finally, collapse each group of contiguous borders into a single side
    groups = {}

    north_sides = 0
    for border in region.north_borders:
        y = border[1]
        if y not in groups:
            groups[y] = []
        groups[y].append(border)
    for group in groups.values():
        north_sides += 1
        group.sort(key=lambda x: x[0])
        for i in range(len(group) - 1):
            if group[i][0] + 1 != group[i + 1][0]:
                north_sides += 1

    #south is exactly the same
    groups = {}
    south_sides = 0
    for border in region.south_borders:
        y = border[1]
        if y not in groups:
            groups[y] = []
        groups[y].append(border)
    for group in groups.values():
        south_sides += 1
        group.sort(key=lambda x: x[0])
        for i in range(len(group) - 1):
            if group[i][0] + 1 != group[i + 1][0]:
                south_sides += 1
    
    #east and west we group by x-coordinary and then sort by y-coordinate
    groups = {}

    east_sides = 0
    for border in region.east_borders:
        x = border[0]
        if x not in groups:
            groups[x] = []
        groups[x].append(border)
    for group in groups.values():
        east_sides += 1
        group.sort(key=lambda x: x[1])
        for i in range(len(group) - 1):
            if group[i][1] + 1 != group[i + 1][1]:
                east_sides += 1

    #west is exactly the same

    groups = {}
    west_sides = 0
    for border in region.west_borders:
        x = border[0]
        if x not in groups:
            groups[x] = []
        groups[x].append(border)
    for group in groups.values():
        west_sides += 1
        group.sort(key=lambda x: x[1])
        for i in range(len(group) - 1):
            if group[i][1] + 1 != group[i + 1][1]:
                west_sides += 1

    region.perimeter = north_sides + south_sides + east_sides + west_sides


# Walk the map. For every cell, if it's not in a region, flood fill a new region starting there 
for y in range(len(input_map)):
    for x in range(len(input_map[y])):
        if (x, y) not in coordinates_to_region.keys():
            # This is a new region
            create_region(x, y, input_map, coordinates_to_region, all_regions)
        #else do nothing

running_total = 0
for region in all_regions:
    calculate_sides(region)
    print(region.id, region.letter, region.area, region.perimeter)
    running_total += region.area * region.perimeter

print(running_total)