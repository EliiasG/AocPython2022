input1, input2 = open("day5\input.txt", "r").read().split("\n\n")

input1 = list(reversed(input1.split("\n")))
l = len(input1.pop(0).replace(" ", ""))
stacks = [[] for i in range(l)]
for line in input1:
    ln = line[1::4]
    for i, char in enumerate(ln):
        if char != " ":
            stacks[i].append(char)

for line in input2.split("\n"):
    amt, frm, to = [int(n) for n in line.split(" ") if n.isnumeric()]
    stacks[to-1] += stacks[frm-1][-amt:]
    for i in range(amt):
        stacks[frm-1].pop()

print("".join([stack[-1] for stack in stacks]))