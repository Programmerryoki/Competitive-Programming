W,P = map(int, input().split())
par = [0] + [int(i) for i in input().split()]+[W]
par.sort()
leng = set()
for i in range(len(par)-1):
    for j in range(1,len(par)):
        if i == j:
            continue
        num = par[j] - par[i]
        if num > 0:
            leng.add(num)
ans = list(leng)
ans.sort()
print(" ".join(map(str, ans)))