import decimal
v,t = input().split()
print(int(decimal.Decimal(v) * decimal.Decimal(t)))