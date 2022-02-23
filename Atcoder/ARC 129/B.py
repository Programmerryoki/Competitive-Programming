from sys import stdin

input = stdin.readline
N = int(input())
p = [-float("inf"), float("inf")]
m = [float("inf"), -float("inf")]
ans = [0]*N
for I in range(N):
    L,R = [int(i) for i in input().split()]
    p[0] = max(p[0], L)
    p[1] = min(p[1], R)
    if L > m[1]:
        m[1] = max(m[1], L)
    if R < m[0]:
        m[0] = min(m[0], R)
    # print(L,R,p,m)
    if p[0] > p[1]:
        ans[I] = -(-(m[1] - m[0]) // 2)
print("\n".join(map(str, ans)))