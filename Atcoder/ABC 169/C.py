import decimal
A,B = input().split()
print(int((int(A)*(decimal.Decimal(B)*decimal.Decimal("100")))//100))