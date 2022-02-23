line = input().split()
H = int(line[0])
if len(line) == 1:
    print(2**(H+1)-1)
else:
    path = line[1]
    root = 2**(H + 1) - 1
    cp = 1
    for m in path:
        if m == "R":
            cp = 2*cp + 1
        else:
            cp = 2*cp
    print(root - cp + 1)