from decimal import Decimal
a,b = [int(i) for i in input().split()]
area = lambda x: x**3*Decimal("0.3333333333") - (a + b)*x**2*Decimal("0.5") + a*b*x
print(abs(area(max(a,b)) - area(min(a,b))))