n, k = [int(i) for i in input().split()]
for a in range(k):
    if n%10 != 0:
        n -= 1
    else:
        n //= 10
print(n)