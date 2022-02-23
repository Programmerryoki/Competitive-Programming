S = input()
r = 1
for s in S:
    r = r * 2 + (s == "R")
print(r)