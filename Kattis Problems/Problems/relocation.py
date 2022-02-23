N,Q = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
ans = []
for i in range(Q):
    n, A,B = [int(i) for i in input().split()]
    if n == 1:
        X[A-1] = B
    else:
        ans.append(abs(X[A-1] - X[B-1]))
print("\n".join(map(str, ans)))