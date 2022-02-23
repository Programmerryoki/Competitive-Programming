from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
N = int(input())
adven = [[], [], []]
seen = set()
for _ in range(N):
    name, *skill = input().split()
    for i in range(3):
        heappush(adven[i], (-int(skill[i]), name))
# print(adven)
group = []
for i in range(0, N, 3):
    if N - i < 3:
        break
    names = []
    for j in range(3):
        skill, name = heappop(adven[j])
        while name in seen:
            skill, name = heappop(adven[j])
        names.append(name)
        seen.add(name)
    names.sort()
    group.append(" ".join(names))
print("\n".join(group))