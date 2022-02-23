from math import gcd

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    if len(set(A)) == 1:
        print(-1)
        continue
    ma = min(A)
    A = [i - ma for i in A if i - ma != 0]
    k = A[0]
    for i in A:
        k = gcd(k, i)
    print(k)