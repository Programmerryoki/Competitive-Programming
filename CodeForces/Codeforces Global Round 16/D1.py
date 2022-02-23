from heapq import heappush, heappop
from bisect import bisect_left
from collections import deque

t = int(input())
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    A = [(A[i], -i) for i in range(n*m)]
    A.sort(reverse=True)
    print(A)
    que = deque()
    a = 0
    inconv = 0
    nxt = []
    for i in range(n):
        order = []
        pe = -1
        for j in range(m):
            if not que:
                print(nxt)
                if nxt:
                    for k in range(len(nxt)-1,-1,-1):
                        que.appendleft(nxt[k])
                    nxt = nxt[:len(nxt)-(m-j)-1]
                else:
                    ev = A[a][0]
                    while a < len(A) and A[a][0] == ev:
                        que.append((-A[a][1], A[a][0]))
                        a += 1
                    while len(que) > m-j:
                        nxt.append(que.popleft())
            index,eye = que.popleft()
            order.append(index)
        print(order)
        tmp = []
        for i in range(m-1,-1,-1):
            ind = bisect_left(tmp, order[i])
            inconv += ind
            tmp.insert(ind, order[i])
    print(inconv)