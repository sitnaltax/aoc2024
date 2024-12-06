def is_digit(input):
    return input.isdigit()

fstream = open("input.txt", 'r')
runningTotal = 0
line = fstream.readline()
left = []
right = []
while line:
    (first, second) = line.split("   ")
    left.append(int(first))
    right.append(int(second))
    line = fstream.readline()

for item in left:
    runningTotal += item * len([x for x in right if x == item])

print(runningTotal)