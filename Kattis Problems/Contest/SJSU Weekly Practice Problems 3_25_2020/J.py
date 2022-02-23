import heapq

n, m = [int(i) for i in input().split()]
city = [{} for i in range(n)]
for _ in range(m):
    a,b,t = [int(i) for i in input().split()]
    city[a-1][b] = t
    city[b-1][a] = t
balls = list(set([int(i) for i in input().split()] + [1]))
tc = 0
INF = 10**6
costs = []
possible = True
for i,a in enumerate(balls):
    que = []
    que.append([0, a])
    cost = [INF]*n
    while len(que) != 0:
        cc, place = heapq.heappop(que)
        # print(place)
        place -= 1
        if cc < cost[place]:
            cost[place] = cc
            for k in city[place].keys():
                tem = city[place][k] + cc
                if cost[k - 1] > tem:
                    heapq.heappush(que, [tem, k])
        # print(que)
        # print(cost)
    # print(a,cost)
    temp = [cost[i-1] for i in balls]
    if INF in temp:
        possible = False
    costs.append(temp)

if possible:
    mi = INF
    def search(total, visited):
        global mi
        pos = [i for i in range(1, len(balls) + 1) if i not in visited]
        # print(total, visited, pos)
        if len(pos) == 0:
            if total < mi:
                mi = total
            return

        for a in pos:
            search(total + costs[visited[-1] - 1][a - 1], visited + [a])

    search(0, [1])
    print(mi)
else:
    print(-1)


# import heapq
#
# n, m = [int(i) for i in input().split()]
# city = [{} for i in range(n)]
# for _ in range(m):
#     a,b,t = [int(i) for i in input().split()]
#     city[a-1][b] = t
#     city[b-1][a] = t
# # print(city)
# balls = list(set(int(i) for i in input().split()))
# curpos = 1
# tc = 0
# INF = 10**6
# while len(balls) != 0:
#     # print(curpos)
#     que = []
#     que.append([0, curpos])
#     cost = [INF]*n
#     while len(que) != 0:
#         # print(que)
#         # print(cost)
#         cc, place = heapq.heappop(que)
#         place -= 1
#         # print(cur)
#         if cc < cost[place]:
#             cost[place] = cc
#             # print(place+1, city[place])
#             for k in city[place].keys():
#                 # print(city[place][k] + cc)
#                 heapq.heappush(que, [city[place][k] + cc, k])
#
#     bc = [cost[b-1] if cost[b-1] != -1 else INF for b in balls]
#     # print(cost)
#     # print(bc,balls)
#     # print()
#     mi = min(bc)
#     curpos = balls.pop(bc.index(mi))
#     tc += mi
# print(tc)