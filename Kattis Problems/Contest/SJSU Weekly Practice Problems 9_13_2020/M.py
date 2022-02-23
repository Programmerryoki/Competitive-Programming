gnum = [1,10]
h = True
while True:
    n = int(input())
    if n == 0:
        break
    res = input()
    if res == "right on":
        print("Stan may be honest" if h and gnum[0] <= n <= gnum[1] else "Stan is dishonest")
        gnum = [1,10]
        h = True
    elif res == "too high":
        gnum[1] = min(n-1, gnum[1])
    elif res == "too low":
        gnum[0] = max(n+1, gnum[0])
    h = gnum[0] <= gnum[1]