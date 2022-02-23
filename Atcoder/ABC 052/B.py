N = int(input())
S = input()
m = 0
c = 0
for s in S:
    if s == "I":
        c += 1
    else:
        c -= 1
    m = max(m, c)
print(m)