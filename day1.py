elves = []
currentelf = 0
largest = 0
topthree = 0

with open("input") as file:
    for line in file:
        values = [line.rstrip() for line in file]
        
for i in values:
    if i == "":
        elves.append(0)
        
for i in values:
    if i == "":
        currentelf += 1
    else:
        elves[currentelf] += int(i)
    if currentelf == 248:
        break

print("Part 1:", max(elves))

for i in range(3):
    topthree += max(elves)
    elves.pop(elves.index(max(elves)))
    
print("Part 2:", topthree)