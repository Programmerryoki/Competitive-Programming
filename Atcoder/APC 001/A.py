from math import gcd
X,Y = map(int, input().split())
print(X*(Y-1) if Y / gcd(X,Y) != 1 else -1)