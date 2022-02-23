N,M = [int(i) for i in input().split()]
graph = {i:set() for i in range(N)}
rgraph = {i:set() for i in range(N)}
for _ in range(M):
    A,B = [int(i)-1 for i in input().split()]
    graph[A].add(B)
    rgraph[B].add(A)

seen = set()
order = []
count = 0

def dfs(cur):
    global seen, order
    for node in graph[cur]:
        if node not in seen:
            seen.add(node)
            dfs(node)
    order.append(cur)

def dfsb(cur):
    global seen, count
    count += 1
    for node in rgraph[cur]:
        if node not in seen:
            seen.add(node)
            dfs(node)

for i in range(N):
    if i in seen:
        continue
    dfs(i)
print(order)
seen.clear()
group = []
for i in order[::-1]:
    if i in seen:
        continue
    count = 0
    dfsb(i)
    group.append(count)
# print(group)
total = 0
for g in group:
    total += ((g-1)*g / 2)
print(int(total))