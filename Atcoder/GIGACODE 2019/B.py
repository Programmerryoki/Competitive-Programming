from sys import stdin
N, X, Y, Z = [int(i) for i in input().split()]
c = 0
for a in stdin:
    s = [int(i) for i in a.split()]
    if s[0] >= X and s[1] >= Y and sum(s) >= Z:
        c += 1
print(c)