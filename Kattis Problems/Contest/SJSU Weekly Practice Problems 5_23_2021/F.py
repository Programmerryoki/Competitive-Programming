while True:
    N = int(input())
    if N == 0:
        break

    pf = [] if N%2 else [2]
    pfb = [] if N%2 or N == 4 else [N//2]
    n = 3
    while n * n <= N:
        if N%n == 0:
            pf.append(n)
            if n * n != N:
                pfb.append(N//n)
        n += 2

    