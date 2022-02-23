N = int(input())
chars = {}
start = ""
la = set()
for i in range(N):
    name, *langs = input().split()
    chars[name] = langs
    la |= set(langs)
# print(chars)
graph = {i:set() for i in la}
for i in chars:
    mainl, *rest = chars[i]
    for j in rest:
        graph[j].add(mainl)
    # if mainl in graph:
    #     graph[mainl] |= set(rest)
    # else:
    #     graph[mainl] = set(rest)
print(graph)

fine = {}
seen = {i:set() for i in graph}

def dfs(start, current, path, see):
    for node in graph[current]:
        if not node in seen[current] and not node in see:
            dfs(start, node, path + [node], see | {node})
        elif node == start:
            print(start,current,path,see)
            ok = path + [node]
            for i in range(len(ok)-1):
                if ok[i] in fine:
                    fine[ok[i]].add(ok[i+1])
                else:
                    fine[ok[i]] = {ok[i+1]}
                seen[ok[i]].add(ok[i+1])
    seen[path[-1]].add(current)

for i in graph:
    dfs(i, i, [i], {i})

print(fine)
print(seen)

count = 0
for i in chars:
    mainl, *rest = chars[i]
    if not mainl in fine:
        print(i)
        count += 1
        continue
    for j in rest:
        if j in fine[mainl]:
            break
    else:
        print(i)
        count += 1
print(count)