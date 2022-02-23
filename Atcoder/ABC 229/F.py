N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
if not N&1:
    even = 0
    odd = 0
    for i in range(N):
        if i&1:
            odd += A[i]
        else:
            even += A[i]
    print(min([odd, even, sum(B)]))
else:
    odd = 0
    even = 0
    for i in range(N):
        if i&1:
            odd += A[i]
        else:
            even += A[i]
    mv = float("inf")
    for i in range(N):
        if not i&1:
            mv = min(mv, odd +  min(A[i], A[(i-1)%N], B[(i-1)%N]))
            odd += A[i]
            even -= A[i]
        else:
            mv = min(mv, even +  min(A[i], A[(i-1)%N], B[(i-1)%N]))
            odd -= A[i]
            even += A[i]
    print(min(mv, sum(B)))