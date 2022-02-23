from fractions import gcd

t = int(input())
for a in range(t):
    n = int(input())
    for num in range(n-1, -1, -1):
        g = gcd(num, n - num)
        if g + (num * (n - num))//g == n:
            print(num, n-num)
            break