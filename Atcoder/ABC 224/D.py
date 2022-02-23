from collections import deque

M = int(input())
graph = {str(i+1) : set() for i in range(9)}
for _ in range(M):
    u,v = input().split()
    graph[u].add(v)
    graph[v].add(u)
tmp = [int(i) for i in input().split()]
p = [0] * 9
for i in range(len(tmp)):
    p[tmp[i]-1] = i+1
# print(p)
goal = " ".join(map(str, [i for i in range(1,9)]+[0]))
que = deque([[0,p.index(0)," ".join(map(str, p))]])
seen = {que[0][2]}
while que:
    cost, zero, tmp = que.popleft()
    if tmp == goal:
        print(cost)
        exit()
    # arr = tmp.split()
    for nxt in graph[str(zero+1)]:
        arr = tmp.split()
        nxt = int(nxt)-1
        arr[nxt],arr[zero] = arr[zero],arr[nxt]
        s = " ".join(arr)
        # arr[nxt],arr[zero] = arr[zero],arr[nxt]
        if s in seen:
            continue
        seen.add(s)
        que.append([cost+1,nxt,s])
print(-1)