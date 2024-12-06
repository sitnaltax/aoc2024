def is_digit(input):
    return input.isdigit()

fstream = open("input.txt", 'r')
runningTotal = 0
line = fstream.readline()
left = []
right = []
while line:
    (first, second) = line.split("   ")
    left.append(first)
    right.append(second)
    line = fstream.readline()
left.sort()
right.sort()

for first, second in zip(left, right):
    runningTotal += abs(int(first) - int(second))
print(runningTotal)