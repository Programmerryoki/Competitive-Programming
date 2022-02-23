N,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
ma = min(A)-1
A = [i - ma for i in A]
print(A)
j = 0
total = 0
ans = 0
for i in range(N):
    print(total + A[i] + (ma * (i-j+1)), K)
    if total + A[i] + (ma * (i-j+1)) < K:
        total += A[i]
    elif total + A[i] + (ma * (i-j+1)) == K:
        total += A[i]
        ans += 1
    else:
        while total + A[i] + (ma * (i-j+1)) > K:
            total -= A[j]
            j += 1
        total += A[i]
        if total + (ma * (i-j+1)) == K:
            ans += 1
print(ans)