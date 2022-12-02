input = open("day2\input.txt", "r").read()
sm = 0
chosenMap = {"A" : "R", "B" : "P", "C" : "S", "X" : "R", "Y" : "P", "Z" : "S"}
beats = {"RS", "SP", "PR"}
score = {"R" : 1, "P" : 2, "S" : 3}
for row in input.split("\n"):
    sp = row.split(" ")
    own = chosenMap[sp[1]]
    other = chosenMap[sp[0]]
    sm += score[own]
    sm += 6 if own + other in beats else (0 if other + own in beats else 3)
print(sm)