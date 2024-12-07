from functools import cmp_to_key

def updateFollowsRules(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

runningTotal = 0
phase = 1
orderingRules = []
updates = []
fstream = open("input.txt", 'r')
line = fstream.readline()
while line:
    if len(line) <=1 :
        phase = 2
    elif phase == 1:
        orderingRules.append(line.strip().split("|"))
    else:
        updates.append(line.strip().split(","))
    line = fstream.readline()

def compareSlow(item1, item2):
    for rule in orderingRules:
        if rule[0] == item1 and rule[1] == item2:
            return -1
        if rule[0] == item2 and rule[1] == item1:
            return 1
    return 0

for update in updates:
    # print("x")
    sortedUpdate = sorted(update, key=cmp_to_key(compareSlow))
    #print(sortedUpdate)
    if sortedUpdate != update:
        #add the middle element to the running total, converted to an integer
        runningTotal += int(sortedUpdate[len(sortedUpdate) // 2])
        
print(runningTotal)