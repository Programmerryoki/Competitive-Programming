from decimal import Decimal

N = int(input())
for a in range(1,10**15):
    n = (-1 + (Decimal(1 + 4 * 1 * 2*a*N))**Decimal(0.5)) / 2
    if n == int(n.as_integer_ratio()[0] / n.as_integer_ratio()[1]):
        print(int(n))
        break