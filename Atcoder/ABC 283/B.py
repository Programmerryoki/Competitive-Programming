N = int(input())
A = [int(i) for i in input().split()]
Q = int(input())
for _ in range(Q):
    n,*rest = input().split()
    if n == "1":
        k,x = rest
        A[int(k)-1] = x
    else:
        k = rest[0]
        print(A[int(k)-1])