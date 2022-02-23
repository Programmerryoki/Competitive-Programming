from sys import stdin
from collections import Counter

cateName = []
cate = []

N = int(input())
for a in range(N):
    line = input().split()
    cateName.append(line[0])
    cate.append(line[2:])


c = Counter()
for a in stdin.readlines():
    a = a[:-1].split()
    c.update(a)

# print(c)
cat = c.keys()
for a in range(len(cate)):
    temp = [c.get(i) for i in cate[a] if i in cat]
    cate[a] = (sum(temp) if len(temp) != 0 else 0)

ans = [[cateName[i], cate[i]] for i in range(len(cate))]
# print(ans)
ans.sort()

ma = max([ans[i][1] for i in range(len(ans))])
for a in range(len(cate)):
    if ans[a][1] == ma:
        print(ans[a][0])

# print(c)
# print(cateName)
# print(cate)