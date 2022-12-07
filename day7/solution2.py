input = open("day7\input.txt", "r").read().split("\n")

curdir = ""
sizes = {}

for line in input:
    split = line.split(" ")
    if split[0] == "$":
        if split[1] == "cd":
            if split[2] == "..":
                oldSize = sizes[curdir]
                curdir = "/".join(curdir.split("/")[:-2]) + "/"
                sizes[curdir] += oldSize
                #print(curdir)
            else:
                curdir += split[2].replace("/","") + "/"
                if curdir not in sizes:
                    sizes[curdir] = 0
                #print(curdir)
                
    elif split[0] != "dir":
        sizes[curdir] += int(split[0])


print(min([i for i in sizes.values() if i > sizes["/"] - 40000000]))
#print(sizes.items())