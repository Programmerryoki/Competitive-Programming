N = int(input())
H = [0]+[int(i) for i in input().split()]+[0]

used = set()
memo = {}
mc = float("inf")
count = 0

def dfs(cost):
    global used, mc, count
    print(cost, used)
    if len(used) == N:
        if cost < mc:
            mc = cost
            count = 1
        elif cost == mc:
            count += 1
        return cost

    mincost = float("inf")
    for i in range(1,N+1):
        if i in used:
            continue
        used.add(i)
        tsu = tuple(sorted(used))
        print(tsu)
        if len(tsu) == N - 1:
            memo[tsu] = min(memo[tsu], dfs(cost + H[i]))
        if tsu not in memo:
            tc = H[i-1] * (i-1 not in used) + H[i] + H[i+1] * (i+1 not in used)
            memo[tsu] = dfs(cost + tc)
        if memo[tsu] < mincost:
            mincost = memo[tsu]
        used.remove(i)
    return mincost

dfs(0)
print(memo, mc)
print(count)