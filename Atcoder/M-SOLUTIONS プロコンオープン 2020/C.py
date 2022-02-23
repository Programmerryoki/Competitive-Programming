N,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
ans = ["Yes" if A[i] > A[i - K] else "No" for i in range(K,N)]
print("\n".join(ans))