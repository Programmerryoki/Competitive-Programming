n, m = [int(i) for i in input().split()]
while True:
    ja = set(input() for i in range(n))
    ji = set(input() for i in range(m))
    print(len(ja & ji))
    n, m = [int(i) for i in input().split()]
    if n == 0 and m == 0:
        break


n,m = [int(i) for i in input().split()]
while True:
    c = 0
    ja = set(int(input()) for i in range(n))
    for a in range(m):
        l = len(ja)
        ja.add(int(input()))
        if l == len(ja):
            c += 1
    print(c)
    n, m = [int(i) for i in input().split()]
    if n == 0 and m == 0:
        break