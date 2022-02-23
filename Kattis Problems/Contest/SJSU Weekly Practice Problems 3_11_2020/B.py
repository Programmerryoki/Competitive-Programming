from collections import defaultdict

m, n = [int(i) for i in input().split()]
dic = []
for a in range(m):
    w, s = input().split()
    dic.append([w, int(s)])

for a in range(n):
    j = defaultdict(int)
    i = input()
    while i != ".":
        for w in i.split():
            j[w] += 1
        i = input()
    s = 0
    for w, v in dic:
        s += j[w] * v
    print(s)