from decimal import Decimal
r,d = [i for i in input().split()]
print((Decimal(d)**2 - Decimal(r)**2)**Decimal(0.5))