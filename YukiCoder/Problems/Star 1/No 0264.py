N,K = [int(i) for i in input().split()]
if N == 2 and K == 0:
    print("Won")
elif N == K:
    print("Drew")
elif K - N == 1:
    print("Won")
else:
    print("Lost")