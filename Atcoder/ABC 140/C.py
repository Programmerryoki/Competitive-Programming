N = int(input())
B = [float("inf")] + [int(i) for i in input().split()] + [float("inf")]
A = 0
for i in range(N):
    A += min(B[i], B[i+1])
print(A)