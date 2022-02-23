n,c = map(int, input().split())
apps = [[int(i) for i in input().split()] + [j+1] for j in range(n)]
apps.sort(key=lambda x: (max(x), x[1], x[0]))
na = 0
cs = 0
for i,na in enumerate(apps):
    d,s,j = na
    if max(d,s) + cs <= c:
        cs += s
    else:
        if i != 0:
            print(i+1)
            print(" ".join(map(str, [j[-1] for j in apps[:i+1]])))
        else:
            print(0)
        break
else:
    print(n)
    print(" ".join(map(str, [j[-1] for j in apps[:i+1]])))