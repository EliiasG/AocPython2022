input = open("day3\input.txt", "r").read().split("\n")

def priority(chr: str) -> int:
    if chr.islower():
        return ord(chr) - ord("a") + 1
    else:
        return ord(chr) - ord("A") + 27

sm = 0
for i in range(0,len(input),3):
    lines = input[i:i+3]
    for c in "".join(lines):
        for line in lines:
            if c not in line:
                break
        else:# else on a for-loop runs when it finsihes without breaking
            sm += priority(c)
            break
print(sm)
