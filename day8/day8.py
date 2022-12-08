import numpy as np

visible = 0
max = 0

with open("day8input.txt") as file:
    it = [line.rstrip() for line in file]
it = [line.split() for line in it]
for i in range(len(it)):
    it[i] = list(map(int, it[i][0]))

check = np.zeros((len(it), len(it)))

for i in range(len(it)):
    max = it[i][0] - 1
    for j in range(len(it)):
        if it[i][j] > max:
            if check[i][j] == 0:
                visible += 1
                check[i][j] = 1
            max = it[i][j]
                
for i in range(len(it)):
    max = it[i][len(it) - 1] - 1
    for j in reversed(range(len(it))):
        if it[i][j] > max:
            if check[i][j] == 0:
                visible += 1
                check[i][j] = 1
            max = it[i][j]

for i in reversed(range(len(it))):
    max = it[len(it) - 1][i] - 1
    for j in reversed(range(len(it))):
        if it[j][i] > max:
            if check[j][i] == 0:
                visible += 1
                check[j][i] = 1
            max = it[j][i]

for i in reversed(range(len(it))):
    max = it[0][i] - 1
    for j in (range(len(it))):
        if it[j][i] > max:
            if check[j][i] == 0:
                visible += 1
                check[j][i] = 1
            max = it[j][i]



print(visible)
print(check)
