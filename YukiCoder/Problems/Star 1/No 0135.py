N = int(input())
X = list(set([int(i) for i in input().split()]))
X.sort()
d = float("INF")
for i in range(1,len(X)):
    d = min(d, X[i] - X[i-1])
print(d if len(X) >= 2 else 0)