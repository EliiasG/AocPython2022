input = open("Day1\input.txt", "r").read()
mx = 0
for elf in input.split("\n\n"):
    sm = 0
    for line in elf.split("\n"):
        sm += int(line)
    mx = max(sm, mx)
print(mx)
