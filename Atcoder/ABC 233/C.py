from collections import defaultdict

N,X = [int(i) for i in input().split()]
bag = []
for _ in range(N):
    L,*rest = [int(i) for i in input().split()]
    t = defaultdict(int)
    for r in rest:
        if r <= X:
            t[r] += 1
    bag.append(t)

ans = 0
def dfs(ind, num, count):
    global fact, ans
    if ind == N:
        if num == 1:
            ans += count
        return
    for n in bag[ind]:
        if num%n == 0:
            dfs(ind+1, num // n, count * bag[ind][n])

dfs(0, X, 1)
print(ans)