input = open("day6\input.txt", "r").read()

for i in range(14,len(input)):
    if len(set(input[i-14:i])) == 14:
        print(i)
        exit()