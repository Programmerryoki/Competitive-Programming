n = int(input())
frac = [[int(i) for i in input().split()] for j in range(n)]
frac.sort(key = lambda x : (x[0]/x[1]), reverse=True)
print("\n".join(" ".join(map(str, i)) for i in frac))