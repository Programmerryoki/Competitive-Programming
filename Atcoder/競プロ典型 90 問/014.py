N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
A.sort()
B.sort()
dif = 0
for i in range(N):
    dif += abs(A[i] - B[i])
print(dif)