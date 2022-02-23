N = int(input())
A = [int(i) for i in input().split()]
A = [(A[i],i+1) for i in range(N)]
A.sort()
print(A[-2][1])