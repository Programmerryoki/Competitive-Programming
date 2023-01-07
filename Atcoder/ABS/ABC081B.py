N = int(input())
A = [int(i) for i in input().split()]
mn = float("inf")
for a in A:
    n = 0
    while a % 2 == 0:
        a //= 2
        n += 1
    mn = min(mn, n)
print(mn)