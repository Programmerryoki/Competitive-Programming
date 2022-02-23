N = int(input())
T = [int(i) for i in input().split()]
st = sum(T)
M = int(input())
for _ in range(M):
    p,x = [int(i) for i in input().split()]
    print(st - T[p - 1] + x)