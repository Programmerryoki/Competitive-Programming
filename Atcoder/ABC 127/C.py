N,M = [int(i) for i in input().split()]
c = [1, N]
for _ in range(M):
    a,b = [int(i) for i in input().split()]
    a,b = min(a,b), max(a,b)
    if c[0] <= a <= b <= c[1]:
        c = [a,b]
    elif a < c[0] <= b < c[1]:
        c = [c[0], b]
    elif c[0] < a <= c[1] < b:
        c = [a, c[1]]
    elif a <= b < c[0]:
        print(0)
        break
    elif c[1] < a <= b:
        print(0)
        break
else:
    print(c[1] - c[0] + 1)