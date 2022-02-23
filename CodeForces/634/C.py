t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    c = {}
    for s in a:
        try:
            c[s] += 1
        except:
            c[s] = 1
    m = max(c.values())
    if m - 1 >= len(c):
        print(len(c))
    elif m == len(c):
        print(len(c)-1)
    elif m == len(c)-1:
        print(len(c)-1)
    else:
        print(m)