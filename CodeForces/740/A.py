t = int(input())
for case in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    sa = list(sorted(A))
    iteration = 0
    while A != sa:
        for i in range(iteration%2, n-1, 2):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                swap = True
        iteration += 1
    print(iteration)