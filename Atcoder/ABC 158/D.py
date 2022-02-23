from collections import deque

S = deque(input())
Q = int(input())
d = 0
for a in range(Q):
    # print(S,d)
    line = input()
    if line[0] == "1":
        d = 1 - d
    else:
        line = line.split()
        if line[1] == "1":
            if d == 1:
                S.append(line[2])
            else:
                S.appendleft(line[2])
        else:
            if d == 1:
                S.appendleft(line[2])
            else:
                S.append(line[2])
if d == 0:
    print("".join(S))
else:
    print("".join(S)[::-1])