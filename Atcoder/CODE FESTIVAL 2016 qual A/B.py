N = int(input())
A = [int(i) for i in input().split()]
pair = 0
for i in range(N):
    if A[A[i]-1]-1 == i:
        pair += 1
print(pair//2)