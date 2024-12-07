
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

for update in updates:
    if updateFollowsRules(update, orderingRules):
        #add the middle element to the running total, converted to an integer
        runningTotal += int(update[len(update) // 2])
        
print(runningTotal)