from itertools import permutations

c = int(input())
graph = {i:set() for i in range(10)}
for _ in range(c):
    a,b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
players = [input().split() for i in range(10)]
for per in permutations([i for i in range(10)], 10):
    pl = [players[i] for i in per]

else:
    print("no")