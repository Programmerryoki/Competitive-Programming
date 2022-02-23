from collections import deque

S = input()
count = 0
br = 0
pot = deque()
dif = 0
for i in range(len(S)):
    if S[i] == "(":
        if pot:
            ind = pot.popleft() + dif
            dif += 1

    elif S[i] == ")":
        pot.append(i)