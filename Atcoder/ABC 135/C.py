N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
t = 0
for i,b in enumerate(B):
    m = min(A[i], b)
    b -= m
    A[i] -= m
    t += m
    m = min(A[i+1], b)
    b -= m
    A[i+1] -= m
    t += m
print(t)