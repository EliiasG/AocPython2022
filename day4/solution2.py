input = open("day4\input.txt", "r").read().split("\n")
sm = 0
def isWithin(mn, mx, n):
    return n >= mn and n <= mx
for line in input:
    mn1, mx1, mn2, mx2 = map(int,line.replace("-", ",").split(","))
    if isWithin(mn2, mx2, mn1) or isWithin(mn2, mx2, mx1) or isWithin(mn1, mx1, mn2) or isWithin(mn1, mx1, mx2):
        sm += 1
        
print(sm)