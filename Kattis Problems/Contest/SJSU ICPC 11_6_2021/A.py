from heapq import heappush, heappop

def main():
    N,*C = [int(i) for i in input().split()]
    V = C.pop()
    que = [[0, [C[0]]+[0]*(N-1)]]
    mc = float("inf")
    seen = {tuple(que[0][1]):0}
    while que:
        cost, cur = heappop(que)
        if cur[0] == V:
            mc = min(mc, cost)
            continue
        serial = tuple(cur)
        if seen[serial] < cost:
            continue
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                pour = min(cur[i], C[j] - cur[j])
                if pour == 0:
                    continue
                tmp = [i for i in cur]
                tmp[i], tmp[j] = tmp[i]-pour, tmp[j]+pour
                serial = tuple(tmp)
                if serial in seen and seen[serial] < cost + pour:
                    continue
                seen[serial] = cost + pour
                heappush(que, [cost + pour, tmp])
    print(mc if mc != float("inf") else "impossible")


if __name__ == '__main__':
    main()

# from threading import Thread, stack_size
# from sys import setrecursionlimit
# setrecursionlimit(10**6)
# stack_size(10**8)
#
#
# def main():
#     N,*C = [int(i) for i in input().split()]
#     V = C.pop()
#
#     liquids = [0]*N
#     liquids[0] = C[0]
#     mincost = float("inf")
#     seen = {}
#     def dfs(cost):
#         nonlocal mincost, liquids
#         if liquids[0] == V:
#             mincost = min(mincost, cost)
#             return
#
#         for i in range(N):
#             for j in range(N):
#                 if i == j:
#                     continue
#                 pour = min(liquids[i], C[j] - liquids[j])
#                 if pour == 0:
#                     continue
#                 liquids[i], liquids[j] = liquids[i]-pour, liquids[j]+pour
#                 serial = "".join("0"*(2-len(str(i)))+str(i) for i in liquids)
#                 if serial in seen and seen[serial] < cost + pour:
#                     liquids[i], liquids[j] = liquids[i]+pour, liquids[j]-pour
#                     continue
#                 seen[serial] = cost + pour
#                 dfs(cost + pour)
#                 liquids[i], liquids[j] = liquids[i]+pour, liquids[j]-pour
#
#     dfs(0)
#     print(mincost if mincost != float("inf") else "impossible")
#
#
# if __name__ == '__main__':
#     tmp = Thread(None, main)
#     tmp.start()
#     tmp.join()