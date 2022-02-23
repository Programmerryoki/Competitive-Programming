T = int(input())
for _ in range(T):
    L,R = map(int, input().split())
    n = max(-1,R - 2*L)
    print((n+1)*(n+2) // 2)