S = input()[::-1]
t = 0
w = 0
for i in range(len(S)):
    if S[i] == "W":
        w += 1
    else:
        t += w
print(t)