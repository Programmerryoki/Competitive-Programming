from collections import deque

N = int(input())
graph = {}
for _ in range(N):
    st = input().split()
    try:
        graph[st[0]].update(set(st[1:]))
    except:
        graph[st[0]] = set(st[1:])
    for n in st[1:]:
        try:
            graph[n].add(st[0])
        except:
            graph[n] = set(st[:1])
# print(graph)
try:
    s,e = input().split()
    que = deque([s])
    path = {s:""}
    seen = set()
    t = ""
    while len(que) != 0:
        t = que.popleft()
        if t == e:
            break
        seen.add(t)
        for n in graph[t]:
            if n not in seen:
                path[n] = t
                que.append(n)
    if t == e:
        ans = deque()
        prev = e
        while prev != "":
            ans.appendleft(prev)
            prev = path[prev]
        print(" ".join(ans))
    else:
        print("no route found")
except:
    print("no route found")