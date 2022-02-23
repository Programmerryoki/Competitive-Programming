from collections import defaultdict, deque
N = int(input())
S = []
startswith = defaultdict(set)
endswith = defaultdict(set)
graph = defaultdict(set)
rgraph = defaultdict(set)
for _ in range(N):
    word = input()
    S.append(word)
    we3 = word[-3:]
    ws3 = word[:3]
    startswith[ws3].add(word)
    endswith[we3].add(word)
    graph[word] |= startswith[we3]
    rgraph[word] |= endswith[ws3]
    for w in endswith[ws3]:
        graph[w].add(word)

print(graph)
print(rgraph)

grundy = {s:1 for s in S}
que = []
for i in range(N):
    if not graph[S[i]]:
        grundy[S[i]] = 0

    win = 0
    for node in graph[S[i]]:
        win += grundy[node]
    if win == len(graph[S[i]]):
        grundy[S[i]] = 0
    elif win == 0:
        grundy[S[i]] = 1
    else:
        grundy[S[i]] = 2
    print(i, win)
print(grundy)
print("\n".join(["Aoki", "Takahashi", "Draw"][grundy[S[i]]] for i in range(N)))

# if not que:
#     print("\n".join(["Draw"] * N))
#     exit()
#
# grundy[que[0]] = 0
# seen = que[0]
# while que:
#     w = que.popleft()
#     for ne in rgraph[w]:
#         if ne not in seen:
#             que.append(ne)
#             grundy[ne] = 1 - grundy[w]
#             seen.add(ne)

