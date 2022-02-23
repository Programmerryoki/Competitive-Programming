from collections import deque

def route(n, K):
    ans = deque()
    while n > 1:
        r = n%K
        ans.appendleft(r)
        if r > 1:
            n = (n + K - r) // K
        else:
            n = (n - r) // K
    return ans

N, K, Q = [int(i) for i in input().split()]
for _ in range(Q):
    x, y = [int(i) for i in input().split()]
    rx = route(x, K)
    ry = route(y, K)
    i = 0
    while i < len(rx) and i < len(ry):
        if rx[i] != ry[i]:
            break
        i += 1
    print(len(rx) + len(ry) - i*2)