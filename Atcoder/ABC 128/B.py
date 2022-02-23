N = int(input())
res = [[i for i in input().split()] + [j+1] for j in range(N)]
res.sort(key = lambda x: (x[0], -int(x[1])))
print("\n".join(str(i[2]) for i in res))