N = int(input())
P = [int(i) for i in input().split()]
ans = [0]*N
for i in range(N):
    ans[P[i]-1] = i+1
print(" ".join(str(i) for i in ans))