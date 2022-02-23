from math import gcd

x = int(input())
for n in range(int(x**0.5),0,-1):
    if x%n == 0 and gcd(n, x//n)==1:
        print(n, x//n)
        break
