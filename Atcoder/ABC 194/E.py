import heapq

N,M = map(int, input().split())
A = [int(i) for i in input().split()]
mi = float("inf")
for i in range(N-M+1):
    lst = list(set(A[i:i+M]))
    # print(lst)
    heapq.heapify(lst)
    count = 0
    while lst and count == lst[0]:
        heapq.heappop(lst)
        count += 1
    # print(count)
    mi = min(count, mi)
print(mi)