n = int(input())
for i in range(n):
    a, b, t = [int(i) for i in input().split()]
    if t in [a+b, abs(a-b), a*b, a/b, b/a]:
        print("Possible")
    else:
        print("Impossible")