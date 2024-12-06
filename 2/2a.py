from enum import Enum

class State(Enum):
    INCREASING = 1
    DECREASING = 2

# returns true if the report is safe
def checkReport(report):
    if report[0] == report[1]:
        return False
    state = State.INCREASING if (report[1] > report[0]) else State.DECREASING
    # iterate through every item but the last one
    for i in range(0, len(report) - 1):
        if state == State.INCREASING:
            if report[i] >= report[i + 1]:
                return False
            if report[i] + 3 < report[i + 1]:
                return False
        else:
            if report[i] <= report[i + 1]:
                return False
            if report[i] - 3 > report[i + 1]:
                return False
    return True

fstream = open("input.txt", 'r')
runningTotal = 0
line = fstream.readline()

while line:
    report = list(map(int, line.split(" ")))
    result = checkReport(report)
    if result:
        print(report)
        runningTotal += 1
    line = fstream.readline()

print(runningTotal)


