from collections import deque

que = deque()
Q = int(input())
ans = []
for _ in range(Q):
    t,x = [int(i) for i in input().split()]
    if t == 1:
        que.appendleft(x)
    elif t == 2:
        que.append(x)
    else:
        ans.append(que[x-1])
print("\n".join(map(str, ans)))