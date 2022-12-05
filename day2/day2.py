opp = []
you = []
score = 0

with open("day2input.txt") as file:
    inpt = [line.rstrip() for line in file]
    
for i in range(len(inpt)):
    opp.append(inpt[i][0])
    you.append(inpt[i][2])

#for i in range(len(inpt)):
 #   if you[i] == "X":
  #      score += 1
   #     if opp[i] == "A":
    #        score += 3
     #   if opp[i] == "C":
      #      score += 6
    #elif you[i] == "Y":
     #   score += 2
      #  if opp[i] == "A":
       #     score += 6
        #if opp[i] == "B":
         #   score += 3
    #else:
     #   score += 3
      #  if opp[i] == "B":
       #     score += 6
        #if opp[i] == "C":
         #   score += 3
#print(score)

for i in range(len(inpt)):
    if opp[i] == "A":
        if you[i] == "X":
            score += 3
        if you[i] == "Y":
            score += 4
        if you[i] == "Z":
            score += 8
    elif opp[i] == "B":
        if you[i] == "X":
            score += 1
        if you[i] == "Y":
            score += 5
        if you[i] == "Z":
            score += 9
    else:
        if you[i] == "X":
            score += 2
        if you[i] == "Y":
            score += 6
        if you[i] == "Z":
            score += 7

print(score)
