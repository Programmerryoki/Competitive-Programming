from fractions import gcd

n = int(input())
for _ in range(n):
    w = int(input())
    ws = [int(i) for i in input().split()]
    c = 1
    for i in ws:
        c = c*i//gcd(c,i)
    if c <= 10**9:
        print(c)
    else:
        print("More than a billion.")