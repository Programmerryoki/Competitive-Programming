import heapq
from sys import stdin

def main():
    input = stdin.readline
    while True:
        N,M,A,K = map(int, input().split())
        if len({N,M,A,K}) == 1 and N == 0:
            break
        graph = {i:{} for i in range(N)}
        for _ in range(M):
            T1,T2,D = map(int, input().split())
            graph[T1-1][T2-1] = D
            graph[T2-1][T1-1] = D
        # defi = {i:{} for i in range(N)}

        ans = [0]*A
        safe = set([i for i in range(N)])
        aliens = [int(input())-1 for i in ans]
        que = []
        seen = set()
        unsafe = set()
        for i,base in enumerate(aliens):
            que.append(base)
            distances = [float("inf")]*N
            distances[base] = 0
            while que:
                node = que.popleft()
                if node in seen:
                    continue
                if distances[node] < K:
                    if node in safe:
                        unsafe.add(node)
                else:
                    seen.add(node)
                    continue
                gn = graph[node]
                for n in gn:
                    if n in seen:
                        continue
                    md = distances[node] + gn[n]
                    if distances[n] > md:
                        distances[n] = md
                    if md < K:
                        que.append(n)
                seen.add(node)
            safe -= unsafe
            ans[i] = len(safe)
            if len(safe) == 0:
                break

            for j in range(N):
                if distances[j] == float("inf"):
                    continue
                if j in graph[base]:
                    if distances[j] < graph[base][j]:
                        graph[base][j] = distances[j]
                        graph[j][base] = distances[j]
                else:
                    graph[base][j] = distances[j]
                    graph[j][base] = distances[j]
                # defi[base][j] = distances[j]
                # defi[j][base] = distances[j]

            que.clear()
            seen.clear()
            unsafe.clear()

        print("\n".join(map(str, ans)))
        print()

if __name__=="__main__":
    main()

# from collections import deque
# from sys import stdin
#
# def main():
#     input = stdin.readline
#     while True:
#         N,M,A,K = map(int, input().split())
#         if len({N,M,A,K}) == 1 and N == 0:
#             break
#         graph = {i:{} for i in range(N)}
#         for _ in range(M):
#             T1,T2,D = map(int, input().split())
#             graph[T1-1][T2-1] = D
#             graph[T2-1][T1-1] = D
#         # defi = {i:{} for i in range(N)}
#
#         ans = [0]*A
#         safe = set([i for i in range(N)])
#         aliens = [int(input())-1 for i in ans]
#         que = deque()
#         seen = set()
#         unsafe = set()
#         for i,base in enumerate(aliens):
#             que.append(base)
#             distances = [float("inf")]*N
#             distances[base] = 0
#             while que:
#                 node = que.popleft()
#                 if node in seen:
#                     continue
#                 if distances[node] < K:
#                     if node in safe:
#                         unsafe.add(node)
#                 else:
#                     seen.add(node)
#                     continue
#                 gn = graph[node]
#                 for n in gn:
#                     if n in seen:
#                         continue
#                     md = distances[node] + gn[n]
#                     if distances[n] > md:
#                         distances[n] = md
#                     if md < K:
#                         que.append(n)
#                 seen.add(node)
#             safe -= unsafe
#             ans[i] = len(safe)
#             if len(safe) == 0:
#                 break
#
#             for j in range(N):
#                 if distances[j] == float("inf"):
#                     continue
#                 if j in graph[base]:
#                     if distances[j] < graph[base][j]:
#                         graph[base][j] = distances[j]
#                         graph[j][base] = distances[j]
#                 else:
#                     graph[base][j] = distances[j]
#                     graph[j][base] = distances[j]
#                 # defi[base][j] = distances[j]
#                 # defi[j][base] = distances[j]
#
#             que.clear()
#             seen.clear()
#             unsafe.clear()
#
#         print("\n".join(map(str, ans)))
#         print()
#
# if __name__=="__main__":
#     main()