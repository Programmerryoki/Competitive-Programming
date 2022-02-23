N = int(input())
A = [int(i) for i in input().split()]
at = [0]+A+[0]
tc = 0
for i in range(N+1):
    tc += abs(at[i]-at[i+1])
ans = [tc]*N
at = at
for i in range(1,N+1):
    if not(at[i+1]<=at[i]<=at[i-1] or at[i-1]<=at[i]<=at[i+1]):
        ans[i-1] -= abs(at[i]-at[i-1]) + abs(at[i+1]-at[i]) - abs(at[i+1]-at[i-1])
print("\n".join(map(str, ans)))