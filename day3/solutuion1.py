input = open("day3\input.txt", "r").read()

def priority(chr: str) -> int:
    if chr.islower():
        return ord(chr) - ord("a") + 1
    else:
        return ord(chr) - ord("A") + 27

sm = 0
for line in input.split("\n"):
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    item = [i for i in first if i in second][0]
    sm += priority(item)
print(sm)
