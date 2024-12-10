fstream = open("input.txt", 'r')
data = fstream.readline()
disk = []
currentFileId = 0
totalDataLength = 0
for i in range(len(data)):
    if i % 2 == 0:
        disk.append([currentFileId] * int(data[i]))
        currentFileId += 1
        totalDataLength += int(data[i])
    else: #append blanks
        disk.append([-1] * int(data[i]))

#flatten the array
disk = [item for sublist in disk for item in sublist]


while len(disk) > totalDataLength:
    item = disk.pop()
    if item != -1:
        disk[disk.index(-1)] = item

print(disk)

checksum = 0
for i in range(len(disk)):
    checksum += i * disk[i]

print(checksum)