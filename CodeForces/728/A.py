t = int(input())
for _ in range(t):
    n = int(input())
    cats = [i+1 for i in range(n)]
    for i in range(0,n - (n&1),2):
        # print(cats)
        cats[i], cats[i+1] = cats[i+1], cats[i]
    if n&1:
        cats[-1], cats[-2] = cats[-2], cats[-1]
    print(" ".join(map(str, cats)))