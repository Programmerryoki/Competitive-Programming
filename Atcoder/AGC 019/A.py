from decimal import Decimal
Q,H,S,D = [int(i) for i in input().split()]
costs = [[Q,Decimal("0.25")], [H,Decimal("0.5")], [S,Decimal("1")], [D,Decimal("2")]]
costs.sort(key=lambda x: Decimal(x[0]) / x[1])
N = int(input())
tc = 0
for c, a in costs:
    tc += c * (N // a)
    N %= a
print(int(tc))