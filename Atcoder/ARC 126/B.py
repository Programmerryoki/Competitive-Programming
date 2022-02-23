from bisect import bisect_right, bisect_left
from sys import stdin
from heapq import heappush, heappop


def main():
    input = stdin.readline
    N,M = [int(i) for i in input().split()]
    lines = [[int(i) for i in input().split()] for _ in range(M)]
    lines.sort()
    used0 = []
    graph0 = {}
    used1 = []
    graph1 = {}
    for i in range(M):
        a,b = lines[i]
        if a not in graph0:
            graph0[a] = []
            used0.append(a)
        graph0[a].append(b)
        if b not in graph1:
            graph1[b] = []
            used1.append(b)
        graph1[b].append(a)
    used0.sort()
    used1.sort()
    # print(lines)
    # print(used0)
    # print(graph0)
    # print(used1)
    # print(graph1)
    all_max = 0
    used = -1
    total = 0
    for i in range(len(used0)):
        x = used0[i]
        ind = bisect_right(graph0[x], used)
        if ind >= len(graph0[x]):
            continue
        total += 1
        used = graph0[x][ind]
    all_max = max(all_max, total)

    # used = N+1
    # total = 0
    # for i in range(len(used0)-1,-1,-1):
    #     x = used0[i]
    #     ind = bisect_left(graph0[x], used)
    #     if ind == 0:
    #         continue
    #     total += 1
    #     used = graph0[x][ind-1]
    # all_max = max(all_max, total)

    used = -1
    total = 0
    for i in range(len(used1)):
        x = used1[i]
        ind = bisect_right(graph1[x], used)
        if ind >= len(graph1[x]):
            continue
        total += 1
        used = graph1[x][ind]
    all_max = max(all_max, total)

    # used = N+1
    # total = 0
    # for i in range(len(used1)-1,-1,-1):
    #     x = used1[i]
    #     ind = bisect_left(graph1[x], used)
    #     if ind == 0:
    #         continue
    #     total += 1
    #     used = graph1[x][ind-1]
    # all_max = max(all_max, total)
    print(all_max)


if __name__ == '__main__':
    main()