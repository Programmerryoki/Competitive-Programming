from collections import deque

n,q=[int(i) for i in input().split()]
que = deque()
for a in range(n):
    s = input().split()
    que.append((s[0], int(s[1])))

t = 0
done = []
while len(que) != 0:
    name, time = que.popleft()
    mi = min(q, time)
    t += mi
    time -= mi
    if time == 0:
        done.append((name, t))
    else:
        que.append((name, time))
for a in done:
    print(a[0], a[1])