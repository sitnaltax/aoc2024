fstream = open("input.txt", 'r')
line = fstream.readline()

stones = []
stones = line.split(" ")

ITERATIONS = 25

for i in range(ITERATIONS):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0: #if the length is even, it becomes two stones, the left half and the right half
            new_stones.append(str(int(stone[:len(stone)//2])))
            new_stones.append(str(int(stone[len(stone)//2:]))) #str->int>->str to remove leading zeroes
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = new_stones

print(len(stones))