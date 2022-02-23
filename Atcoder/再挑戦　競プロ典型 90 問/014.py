N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
A.sort()
B.sort()
print(sum(abs(A[i]-B[i]) for i in range(N)))