from bisect import bisect_left
from collections import defaultdict
from sys import setrecursionlimit, stdin
setrecursionlimit(10**8)


def main():
    input = stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        aliens = [[int(i) for i in input().split()] for j in range(n)]
        aliens.sort(key=lambda x: (x[1], x[0]))
        times = [i[1] for i in aliens]
        A = []
        for i,[a,b,d] in enumerate(aliens):
            index = bisect_left(times, a)
            A.append(tuple([index, i]))
        m = float("inf")

        def recur(pc, i, de):
            nonlocal m
            if i == n:
                des = defaultdict(set)
                for j in range(n):
                    des[pc[j]].add(aliens[j][-1])
                cost = 0
                for key in des:
                    cost += max(des[key])
                m = min(m, cost)
                return

            for p in range(A[i][0], A[i][1]+1):
                if p not in de:
                    if p != i:
                        recur(pc + [p], i+1, de | {i})
                    else:
                        recur(pc + [p], i+1, de)

        recur([], 0, set())
        print(m)
if __name__ == "__main__":
    main()


# from bisect import bisect_left
# from collections import defaultdict
# from sys import setrecursionlimit, stdin
# setrecursionlimit(10**8)
#
#
# def main():
#     input = stdin.readline
#     T = int(input())
#     for _ in range(T):
#         n = int(input())
#         aliens = [[int(i) for i in input().split()] for j in range(n)]
#         aliens.sort(key=lambda x: (x[1], x[0]))
#         times = [i[1] for i in aliens]
#         A = []
#         for i,[a,b,d] in enumerate(aliens):
#             index = bisect_left(times, a)
#             A.append(tuple([index, i]))
#         m = float("inf")
#
#         def recur(pc, i, de):
#             # print(pc,i,de)
#             nonlocal m
#             if i == n:
#                 des = defaultdict(set)
#                 for j in range(n):
#                     des[pc[j]].add(j)
#                 cost = 0
#                 for key in des:
#                     cost += max([aliens[j][-1] for j in des[key]])
#                 m = min(m, cost)
#                 return
#
#             for p in range(A[i][0], A[i][1]+1):
#                 if p not in de:
#                     if p != i:
#                         recur(pc + [p], i+1, de | {i})
#                     else:
#                         recur(pc + [p], i+1, de)
#
#         recur([], 0, set())
#         print(m)
# if __name__ == "__main__":
#     main()


# from collections import defaultdict
# from bisect import bisect_left
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     aliens = [[int(i) for i in input().split()] for j in range(n)]
#     aliens.sort(key=lambda x: (x[1], x[0]))
#     times = [i[1] for i in aliens]
#     A = {i:set() for i in range(n)}
#     for i,[a,b,d] in enumerate(aliens):
#         index = bisect_left(times, a)
#         for j in range(index, i+1):
#             A[j].add(i)
#     # print(A, times)
#     des = set()
#     tc = 0
#     for i in range(len(A)):
#         if i not in des:
#             tc += max([0] + [aliens[j][-1] for j in A[i] if j not in des])
#             des.update(A[i])
#     print(tc)