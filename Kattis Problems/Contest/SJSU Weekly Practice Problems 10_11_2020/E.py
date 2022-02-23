n,M = [int(i) for i in input().split()]
od = float("inf")
for _ in range(n):
    p,c = map(int, input().split())
    od = min(od, (M+c)//p)
print(od)