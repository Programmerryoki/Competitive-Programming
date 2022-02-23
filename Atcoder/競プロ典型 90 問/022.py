from math import gcd

A,B,C = map(int, input().split())
m = gcd(gcd(A,B), C)
A,B,C = [i // m for i in (A,B,C)]
print(A-1 + B-1 + C-1)