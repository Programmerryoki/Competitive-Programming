N, M, Q = [int(i) for i in input().split()]
pos = []
for _ in range(Q):
    pos.append([int(i) for i in input().split()])
pos.sort(key = lambda x: x[-1], reverse=True)

ans = [1]*N
for a,b,c,d in pos:
