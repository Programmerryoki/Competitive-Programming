from collections import defaultdict, deque

n = int(input())
move = {"N":[0,1], "E":[1,0], "S":[0,-1], "W":[-1,0]}
poss = [[0,1], [1,0], [0,-1], [-1,0]]
for _ in range(n):
    input()
    s = int(input())
    graph = defaultdict(set)
    mm = [input() for i in range(s)]
    pos = tuple([0,0])
    for m in mm:
        dx,dy = move[m]
        t = tuple([pos[0]+dx, pos[1]+dy])
        graph[pos].add(t)
        graph[t].add(pos)
        pos = t
    s = tuple([0,0]); e = pos
    # for i in graph:
    #     print(i, graph[i])
    # print(s,e)
    if s == e:
        print(0)
        continue
    que = deque([[s, 0]])
    went = {s}
    while que:
        # print(que)
        node, d = que.popleft()
        for p in graph[node]:
            if p == e:
                print(d+1)
                s = p
                break
            if p not in went:
                que.append([p, d+1])
                # print(p,d+1)
                went.add(p)
        if s == e:
            break

# import heapq
# from collections import defaultdict
#
# n = int(input())
# move = {"N":[0,1], "E":[1,0], "S":[0,-1], "W":[-1,0]}
# poss = [[0,1], [1,0], [0,-1], [-1,0]]
# for _ in range(n):
#     input()
#     s = int(input())
#     graph = defaultdict(set)
#     mm = [input() for i in range(s)]
#     pos = tuple([0,0])
#     for m in mm:
#         dx,dy = move[m]
#         t = tuple([pos[0]+dx, pos[1]+dy])
#         graph[pos].add(t)
#         graph[t].add(pos)
#         pos = t
#     s = tuple([0,0]); e = pos
#     # for i in graph:
#     #     print(i, graph[i])
#     # print(s,e)
#     path = []
#     dis = []
#     went = {s}
#     while s != e:
#         # print(graph[s])
#         for p in graph[s]:
#             if p not in went and p in graph:
#                 heapq.heappush(dis, [(abs(p[0]-e[0])+abs(p[1]-e[1])),p])
#                 went.add(p)
#         # print(dis)
#         d,s = heapq.heappop(dis)
#         path.append(s)
#         # print(d,s)
#     print(path)
#     print(len(path))

# n = int(input())
# move = {"N":[0,1], "E":[1,0], "S":[0,-1], "W":[-1,0]}
# for _ in range(n):
#     input()
#     s = int(input())
#     mm = [input() for i in range(s)]
#     path = [[0,0]]
#     went = set()
#     went.add(tuple([0,0]))
#     for m in mm:
#         dx,dy = move[m]
#         x,y = path[-1][0]+dx, path[-1][1]+dy
#         if tuple([x,y]) in went:
#             path = path[:path.index([x,y])]
#             went = set([tuple(i) for i in path])
#         else:
#             went.add(tuple([x,y]))
#         path.append([x,y])
#     print(len(path)-1)