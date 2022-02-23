N,K = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
total = 0
for i in range(N):
    total += abs(A[i]-B[i])
print("Yes" if total == K or (total < K and (K - total) % 2 == 0) else "No")