from decimal import Decimal

cx,cy,n = map(int, input().split())
dist = []
for _ in range(n):
    x,y,r = map(Decimal, input().split())
    dist.append(max(0, ((cx-x)**2+(cy-y)**2).sqrt() - r))
dist.sort()
print(int(dist[2]))