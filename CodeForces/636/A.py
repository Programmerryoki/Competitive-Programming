N = int(input())
for _ in range(N):
    n = int(input())
    i = 2
    while n%(2**i - 1) != 0:
        i += 1
    print(n//(2**i - 1))