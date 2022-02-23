N,M = map(int, input().split())
from1 = set()
ton = set()
for _ in range(M):
    a,b = map(int, input().split())
    if 1 in [a,b]:
        from1.add(a)
        from1.add(b)
    if N in [a,b]:
        ton.add(a)
        ton.add(b)
print("POSSIBLE" if from1 & ton else "IMPOSSIBLE")