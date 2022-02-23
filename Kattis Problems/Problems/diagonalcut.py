import math

M, N = [int(i) for i in input().split()]
gcd = math.gcd(M, N)
M, N = M // gcd, N // gcd
if M % 2 == N % 2 and M % 2 == 1:
    print(gcd)
else:
    print(0)