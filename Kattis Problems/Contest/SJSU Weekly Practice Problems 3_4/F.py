while True:
    n,t = [float(i) for i in input().split()]
    if n == t == 0:
        break
    print(2**n * t**n)