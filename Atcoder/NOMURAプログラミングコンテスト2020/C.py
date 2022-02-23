N = int(input())
A = [int(i) for i in input().split()]
n = 1
t = 0
for i,a in enumerate(A):
    if n < a:
        print(-1)
        break

    n -= a
    n *= 2

else:
    print(t)