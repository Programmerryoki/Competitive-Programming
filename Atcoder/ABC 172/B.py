S = input()
T = input()
c = 0
for i in range(len(S)):
    if S[i] != T[i]:
        c += 1
print(c)