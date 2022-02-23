T = int(input())
for _ in range(T):
    n,m = [int(i) for i in input().split()]
    h = [int(input()) for i in range(m)]
    h.sort()
    print([h[i+1] - h[i] for i in range(m-1)])