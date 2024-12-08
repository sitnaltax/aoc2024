import pdb

def parse_map(input_map):
    antennas = {}
    for y, line in enumerate(input_map.strip().split('\n')):
        for x, char in enumerate(line):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    print(antennas)

    return antennas

def calculate_antinodes(antennas, width, height):
    antinodes = set()
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                antinode_x1 = x1 - (x2 - x1)
                antinode_y1 = y1 - (y2 - y1)
                antinode_x2 = x2 + (x2 - x1)
                antinode_y2 = y2 + (y2 - y1)
                if 0 <= antinode_x1 < width and 0 <= antinode_y1 < height:
                    antinodes.add((antinode_x1, antinode_y1))
                if 0 <= antinode_x2 < width and 0 <= antinode_y2 < height:
                    antinodes.add((antinode_x2, antinode_y2))
        print(freq)
        print(antinodes)
    return antinodes

def count_unique_antinodes(input_map):
    lines = input_map.strip().split('\n')
    width = len(lines[0])
    height = len(lines)
    antennas = parse_map(input_map)
    antinodes = calculate_antinodes(antennas, width, height)
    return len(antinodes)

input_map = ""
fstream = open("input.txt", 'r')
line = fstream.readline()
while line:
    input_map += line
    line = fstream.readline()

print(count_unique_antinodes(input_map))