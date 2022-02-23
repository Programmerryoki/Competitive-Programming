from math import gcd

A,B = [int(i) for i in input().split()]
ans = A * B // gcd(A, B)
print(ans if ans <= 10**18 else "Large")