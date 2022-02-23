N,M = map(int, input().split())
X = [int(i) for i in input().split()]
X.sort()
xd = [int(X[i] - X[i-1]) for i in range(1,M)]
xd.sort(reverse=True)
print(sum(xd[N-1:]))