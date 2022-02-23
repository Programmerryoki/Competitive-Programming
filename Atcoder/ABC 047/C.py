S = input()
w = S[0]
c = 0
for a in S:
    if a != w:
        c += 1
        w = a
print(c)