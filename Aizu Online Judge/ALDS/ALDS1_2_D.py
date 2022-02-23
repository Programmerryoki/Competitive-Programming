cnt = 0

def IS(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v

n = int(input())
A = [int(input()) for _ in range(n)]
m = 
G =
for i in range(0, m):
    IS(A, n, G[i])