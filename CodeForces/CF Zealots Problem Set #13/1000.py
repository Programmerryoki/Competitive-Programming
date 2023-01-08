t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    tile = input()
    nb = 0
    for i in range(k-1):
        nb += tile[i] == "B"
    mw = float("inf")
    for i in range(k-1,n):
        nb += (tile[i] == "B")
        mw = min(mw, k-nb)
        nb -= (tile[i-k+1] == "B")
    print(mw)