fstream = open("input.txt", 'r')
line = fstream.readline()

initial_stones = line.split(" ")

ITERATIONS = 75

def add_stone(stone, count, dict):
    if dict.get(stone) == None:
        dict[stone] = count
    else:
        dict[stone] += count

stones = {}
for stone in initial_stones:
    add_stone(stone, 1, stones)

for i in range(ITERATIONS):
    new_stones = {}
    for stone, num in stones.items():
        if stone == "0":
            add_stone("1", num, new_stones)
        elif len(stone) % 2 == 0: #if the length is even, it becomes two stones, the left half and the right half
            add_stone((str(int(stone[:len(stone)//2]))), num, new_stones)
            add_stone((str(int(stone[len(stone)//2:]))), num, new_stones) #str->int->-str to remove leading zeroes
        else:
            add_stone((str(int(stone) * 2024)), num, new_stones)
    stones = new_stones
    print(stones)

#add up all the values in the dictionary
print(sum(stones.values()))
