N = int(input())
A = [int(i) for i in input().split()]
A.sort()
print("{:.1f}".format(float(A[N//2]))) if N&1 else print("{:.1f}".format((A[N//2] + A[N//2-1])/2))