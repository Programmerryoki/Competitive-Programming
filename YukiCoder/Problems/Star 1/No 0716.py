N = int(input())
A = [int(i) for i in input().split()]
A.sort()
ad = [A[i] - A[i-1] for i in range(1,len(A))]
print(min(ad))
print(max(A) - min(A))