n, d = [int(i) for i in input().split()]
while n != 0 or d != 0:
    print(n//d, n%d, "/", d)
    n, d = [int(i) for i in input().split()]