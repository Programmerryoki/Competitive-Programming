from collections import deque

TC = int(input())
ans = []
for _ in range(TC):
    input()

    V = int(input())
    graph = {i:{} for i in range(V)}
    for j in range(V):
        x, *pairs = [int(i) for i in input().split()]
        for i in range(0,len(pairs),2):
            graph[j][pairs[i]] = pairs[i+1]
    # print(graph)
    temp = []
    Q = int(input())
    for _ in range(Q):
        s,t,k = [int(i) for i in input().split()]

        mt = float("inf")
        que = deque([[s, 0, 1]])
        while que:
            node, cost, jn = que.popleft()
            if jn > k:
                continue
            if node == t:
                mt = min(mt, cost)
                continue

            for n in graph[node]:
                que.append([n, cost + graph[node][n], jn+1])

        temp.append(mt)
    ans.append(temp)
print("\n\n".join("\n".join(map(str, i)) for i in ans))

# TC = int(input())
# ans = []
# for _ in range(TC):
#     input()
#
#     V = int(input())
#     graph = {i:{} for i in range(V)}
#     for j in range(V):
#         x, *pairs = [int(i) for i in input().split()]
#         for i in range(0,len(pairs),2):
#             graph[j][pairs[i]] = pairs[i+1]
#     # print(graph)
#     temp = []
#     Q = int(input())
#     for _ in range(Q):
#         s,t,k = [int(i) for i in input().split()]
#
#         mt = float("inf")
#         def dfs(c, jn, cost):
#             # print(c,jn,cost)
#             global mt
#             if jn > k:
#                 return
#             if c == t:
#                 mt = min(mt, cost)
#                 return
#
#             for node in graph[c]:
#                 dfs(node, jn+1, cost+graph[c][node])
#         # print("\t",s,t,k)
#         dfs(s, 1, 0)
#         temp.append(mt)
#     ans.append(temp)
# print("\n\n".join("\n".join(map(str, i)) for i in ans))