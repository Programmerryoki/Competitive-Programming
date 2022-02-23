N = int(input())
A = [int(input()) for i in range(N)]
m1 = max(A[0], A[1])
m2 = min(A[0], A[1])
for i in range(2,N):
    if m1 < A[i]:
        m1, m2 = A[i], m1
    elif m2 < A[i]:
        m2 = A[i]
print("\n".join(map(str, [m1 if i != m1 else m2 for i in A])))