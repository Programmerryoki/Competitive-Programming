N = int(input())
exps = [[j,[int(i) for i in input().split()]] for j in range(N)]
exps.sort(key = lambda x : x[1][0] - 30000*x[1][1], reverse=True)
best = exps[0]
exp = best[1][0] - 30000*best[1][1]
if exp*6 >= 30000*100:
    print("YES")
    print("\n".join([str(best[0] + 1)]*6))
else:
    print("NO")