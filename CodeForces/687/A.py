t = int(input())
for _ in range(t):
    n,m,r,c = map(int, input().split())
    print(max(r-1, n-r) + max(c-1, m-c))