N = int(input())
A = [int(i) for i in input().split()]
ans = [0]*N
for a in range(len(A)-1,-1,-1):
    ans[A[a]-1] += 1
for a in ans:
    print(a)