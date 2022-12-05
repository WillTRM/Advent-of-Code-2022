import re
import numpy
import os
import time

toggledisplay = 1

with open("day5input.txt") as file:
    instruct = [line.rstrip() for line in file]
    
field = []
grabbed = ""
stack = []

um = """[W] [V]     [P]                    
[B] [T]     [C] [B]     [G]        
[G] [S]     [V] [H] [N] [T]        
[Z] [B] [W] [J] [D] [M] [S]        
[R] [C] [N] [N] [F] [W] [C]     [W]
[D] [F] [S] [M] [L] [T] [L] [Z] [Z]
[C] [W] [B] [G] [S] [V] [F] [D] [N]
[V] [G] [C] [Q] [T] [J] [P] [B] [M]"""

field = re.findall("[A-Z]|\s{4}", um)

for i in range(len(field)):
    field[i] = field[i].strip()
    
field = numpy.array(field)
field = field.reshape(8, 9)

field = numpy.pad(field, [(48, 0), (0, 0)], mode = "constant", constant_values = "")

for i in range(len(instruct)):
    instruct[i] = re.findall("\d+", instruct[i])
       
def showfield(display):
    os.system("printf '\033c'")
    print(display)
    time.sleep(0.01)

if int(input("1 for part 1, 2 for part 2: ")) == 1:
    for j in range(len(instruct)):
        for i in range(int(instruct[j][0])):
            claw = 0
            while field[claw][int(instruct[j][1]) - 1] == "":
                claw += 1
            grabbed = field[claw][int(instruct[j][1]) - 1]
            field[claw][int(instruct[j][1]) - 1] = ""
            claw = 0
            while field[claw][int(instruct[j][2]) - 1] == "":
                claw += 1
                if claw == 56:
                    break
            claw -= 1
            field[claw][int(instruct[j][2]) - 1] = grabbed
        if toggledisplay == 1:
            showfield(field)
    for i in range(9):
        claw = 0
        while field[claw][i] == "":
            claw += 1
        print(field[claw][i], end = "")
    
else:
    for j in range(len(instruct)):
        for i in range(int(instruct[j][0])):
            claw = 0
            while field[claw][int(instruct[j][1]) - 1] == "":
                claw += 1
            stack.append(field[claw][int(instruct[j][1]) - 1])
            field[claw][int(instruct[j][1]) - 1] = ""
            claw = 0
        for i in range(int(instruct[j][0])):
            while field[claw][int(instruct[j][2]) - 1] == "":
                claw += 1
                if claw == 56:
                    break
            claw -= 1
            field[claw][int(instruct[j][2]) - 1] = stack[-1]
            stack.pop(-1)
        if toggledisplay == 1:
            showfield(field)
    for i in range(9):
        claw = 0
        while field[claw][i] == "":
            claw += 1
        print(field[claw][i], end = "")
