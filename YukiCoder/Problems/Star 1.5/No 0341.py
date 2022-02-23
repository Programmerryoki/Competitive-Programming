S = input()
m = 0
c = 0
for s in S:
    if s == "…":
        c += 1
    else:
        m = max(m, c)
        c = 0
print(max(m, c))