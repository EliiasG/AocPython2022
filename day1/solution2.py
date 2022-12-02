input = open("day1\input.txt", "r").read()
cal = []
for elf in input.split("\n\n"):
    sm = 0
    for line in elf.split("\n"):
        sm += int(line)
    cal.append(sm)
print(sum(sorted(cal)[-3:]))
