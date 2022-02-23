N, K = [int(i) for i in input().split()]
A = [int(i)%K for i in input().split()]
# print(A)
c = 0
for a in range(1,K):
    # print(A[0:a])
    total = sum(A[0:a])
    for b in range(len(A)-a+1):
        # print(total, a, b, a+b, c)
        if total%K == a:
            c += 1
        total -= A[b]
        if a+b < len(A):
            total += A[b+a]
print(c)