from heapq import heapify, heappop

N = int(input())
a = [int(i) for i in input().split()]
ans = []
heap = [[a[i], i] for i in range(N)]
prev = -1
heapify(heap)
while heap:
    val, ind = heappop(heap)
    if ind > prev:
        continue
    ans.append(val)
print(" ".join(str(i) for i in ans))