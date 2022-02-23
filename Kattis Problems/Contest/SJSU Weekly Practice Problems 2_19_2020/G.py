N = int(input())
ns = [int(i) for i in input().split()]
M = int(input())
ms = [int(i) for i in input().split()]
mi = 100000
for a in ns:
    line = input().split()
    for j in line:
        p = a + ms[int(j) - 1]
        if p < mi:
            mi = p
X = int(input())
print(max(X//mi-1, 0))