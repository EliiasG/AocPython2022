input = open("day2\input.txt", "r").read()
sm = 0
chosenMap = {"A" : "R", "B" : "P", "C" : "S"}
beats = {"RS", "SP", "PR"}
score = {"R" : 1, "P" : 2, "S" : 3}
chooseMap = {"XR" : "S", "XP" : "R", "XS" : "P", "YR" : "R" , "YP" : "P", "YS" : "S", "ZR" : "P", "ZP" : "S", "ZS" : "R"}
for row in input.split("\n"):
    sp = row.split(" ")
    other = chosenMap[sp[0]]
    own = chooseMap[sp[1] + other]
    sm += score[own]
    sm += 6 if own + other in beats else (0 if other + own in beats else 3)
print(sm)