N = int(input())
ans = [int(i) for i in input().split()]
m = max(ans)
n = ans.count(m)
if n == N:
    if ans[0]//(N-1) == 2:
        print(n, N-n)
    else:
        print(N - n, n)
else:
    print(n, N - n)