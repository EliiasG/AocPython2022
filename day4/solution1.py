input = open("day4\input.txt", "r").read().split("\n")
sm = 0
for line in input:
    mn1, mx1, mn2, mx2 = map(int,line.replace("-", ",").split(","))
    for dat in [[mn1, mx1, mn2, mx2], [mn2, mx2, mn1, mx1]]:
        if dat[0] >= dat[2] and dat[1] <= dat[3]:
            sm += 1
            break
print(sm)