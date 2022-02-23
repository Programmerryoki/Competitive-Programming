from sys import stdin
ans = []
lines = stdin.readlines()
index = 0
while index < len(lines):
    line = ""
    log = []
    while index < len(lines) and line != "\n":
        # print(line)
        line = lines[index]
        log.append(line)
        index += 1
    log = log[::-1]
    # print(log)
    i = 0
    for a in range(len(log)):
        c = log[a].count("*")
        log[a] = "."*i + "*"*c + "."*(len(log[a])-i-c-1)
        i += c
    # print(log)
    ans.append(log[::-1])
    # print("Done")

for i,a in enumerate(ans):
    print("\n".join(a))
    # if i != len(ans)-1:
    #     print()