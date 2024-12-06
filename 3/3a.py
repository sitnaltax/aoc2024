import re

fstream = open("input.txt", 'r')
runningTotal = 0
line = fstream.readline()

while line:
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    results = pattern.findall(line)
    for item in results:
        runningTotal += int(item[0]) * int(item[1])
        
    line = fstream.readline()
print(runningTotal)