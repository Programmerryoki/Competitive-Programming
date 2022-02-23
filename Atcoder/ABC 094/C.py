N = int(input())
X = [int(i) for i in input().split()]
ori = [i for i in X]
X.sort()
ans = [0]*N
mid = X[N//2]
for i in range(N):
    if ori[i] >= mid:
        ans[i] = X[N//2-1]
    else:
        ans[i] = X[N//2+(ori[i]==X[N//2])]
print("\n".join(map(str, ans)))