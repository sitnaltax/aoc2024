fstream = open("input.txt", 'r')
data = fstream.readline()
disk = []
currentFileId = 0
totalDataLength = 0
fileLocations = {}
fileLengths = {}
position = 0
for i in range(len(data)):
    if i % 2 == 0:
        fileLocations[currentFileId] = position
        fileLengths[currentFileId] = int(data[i])
        disk.append([currentFileId] * int(data[i]))
        currentFileId += 1
        totalDataLength += int(data[i])
    else: #append blanks
        disk.append([-1] * int(data[i]))
    position += int(data[i])

# flatten the array
disk = [item for sublist in disk for item in sublist]

#Instead of popping the last element, iterate through the files in reverse order and try to move
# each one to the first blank space it fits

def find_sequence(lst, seq):
    seq_len = len(seq)
    for i in range(len(lst) - seq_len + 1):
        if lst[i:i + seq_len] == seq:
            return i
    return -1

for i in range(currentFileId - 1, -1, -1):
    # find the first block of consecutive -1s that's long enough
    start = find_sequence(disk, [-1] * fileLengths[i])
    if start == -1 or start > fileLocations[i]:
        continue
    for j in range(start, start + fileLengths[i]):
        disk[j] = i
    for j in range(fileLocations[i], fileLocations[i] + fileLengths[i]):
        disk[j] = -1

checksum = 0
for i in range(len(disk)):
    if disk[i] != -1:
        checksum += i * disk[i]

print(checksum)