from math import ceil

MOD = 10**9 + 7
N = int(input())
t = 0
for _ in range(N):
    c,d = map(int, input().split())
    t += ((c+1)//2) * d
    t %= MOD
print(t)