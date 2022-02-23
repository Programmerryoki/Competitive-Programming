from collections import deque

N, X, Y = [int(i) for i in input().split()]
X -= 1
Y -= 1
ans = [0 for i in range(N)]
INF = 1000000000
for i in range(N):
    dist = [INF for i in range(N)]
    q = deque()
    def push(v,d):
        if dist[v] != INF:
            return
        dist[v] = d
        q.append(v)
    push(i, 0)
    while len(q) != 0:
        v = q.popleft()
        d = dist[v]
        if v-1 >= 0:
            push(v-1, d+1)
        if v+1 < N:
            push(v+1, d+1)
        if v == X:
            push(Y, d+1)
        if v == Y:
            push(X,d+1)
    for j in range(N):
        ans[dist[j]] += 1
for i in range(N):
    ans[i] //= 2
print("\n".join(map(str, ans[1:])))

# N, X, Y = [int(i) for i in input().split()]
# X, Y = min(X, Y), max(X, Y)
# for k in range(1,N):
#     total = [set() for i in range(N)]
#     for i in range(1,N+1):
#         pos = set()
#         if i + k <= N:
#             if i+k not in total[i-1]:
#                 # total[i+k-1].add(i)
#                 pos.add(i+k-1)
#         if i - k >= 1:
#             if i-k not in total[i-1]:
#                 # total[i-k-1].add(i)
#                 pos.add(i-k-1)
#         if i <= X:
#             if i + k > X:
#                 j = k - (X - i) - 1
#                 if Y + j <= N:
#                     if Y+j not in total[i-1]:
#                         # total[Y+j-1].add(i)
#                         pos.add(Y+j-1)
#                 if Y - j > X + j:
#                     if Y - j not in total[i-1]:
#                         # total[Y-j-1].add(i)
#                         pos.add(Y-j-1)
#         elif i <= Y:
#             if i + k > Y:
#                 j = k - (Y - i) - 1
#                 if X + j <= Y - j:
#                     if X+j not in total[i-1]:
#                         # total[X+j-1].add(i)
#                         pos.add(X+j-1)
#                 if X - j > 0:
#                     if X - j not in total[i-1]:
#                         # total[X-j-1].add(i)
#                         pos.add(X-j-1)
#             if i - k < X:
#                 j = k - (X - i) - 1
#                 if Y + j <= N:
#                     if Y+j not in total[i-1]:
#                         # total[Y+j-1].add(i)
#                         pos.add(Y+j-1)
#                 if Y - j > X + j:
#                     if Y - j not in total[i-1]:
#                         # total[Y-j-1].add(i)
#                         pos.add(Y-j-1)
#         else:
#             if i - k < Y:
#                 j = k - (Y - i) - 1
#                 if X + j <= Y - j:
#                     if X+j not in total[i-1]:
#                         # total[X+j-1].add(i)
#                         pos.add(X+j-1)
#                 if X - j > 0:
#                     if X - j not in total[i-1]:
#                         # total[X-j-1].add(i)
#                         pos.add(X-j-1)
#         for j in pos:
#             total[j].add(i)
#     print(total)
#     s = 0
#     for t in total:
#         s += len(t)
#     print(s)