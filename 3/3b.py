import re

fstream = open("input.txt", 'r')
runningTotal = 0
line = fstream.readline()
allInput = ""
while line:
    allInput += line
    line = fstream.readline()

#Process the input by removing everything in between a don't() and the next do()
def processInput(input):
    while "don't()" in input:
        start = input.find("don't()")
        end = input.find("do()", start)
        print(start, end)
        if end < 0:
            return input[:start]
        input = input[:start] + input[end + 4:]
    return input

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
results = pattern.findall(processInput(allInput))
for item in results:
    runningTotal += int(item[0]) * int(item[1])
        
print(runningTotal)