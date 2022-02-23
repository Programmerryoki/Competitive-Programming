N = int(input())
graph = {}
rgraph = {}
lang = {}
for _ in range(N):
    name, *rest = input().split()
    mother, *other = rest
    for i in other:
        if i not in lang:
            lang[i] = set()
    if mother not in lang:
        lang[mother] = set()
    lang[mother].add(name)

    if mother not in graph:
        graph[mother] = {mother}
    if mother not in rgraph:
        rgraph[mother] = {mother}
    for i in other:
        if i not in graph:
            graph[i] = {i}
        if i not in rgraph:
            rgraph[i] = {i}
        graph[i].add(mother)
        rgraph[mother].add(i)

order = []
seen = set()
def dfs(cur):
    global seen
    for nxt in graph[cur]:
        if nxt not in seen:
            seen.add(nxt)
            dfs(nxt)
    order.append(cur)

for i in lang:
    if i in seen:
        continue
    seen.add(i)
    dfs(i)
# print(order)

seen.clear()
max_group = 0
for l in order[::-1]:
    if l in seen:
        continue
    seen.add(l)
    stack = [l]
    group = []
    while stack:
        cur = stack.pop()
        for nxt in rgraph[cur]:
            if nxt not in seen:
                stack.append(nxt)
                seen.add(nxt)
        group.append(cur)
    n = set()
    for i in group:
        if i in lang:
            n |= lang[i]
    if len(n) > max_group:
        max_group = len(n)
print(N - max_group)