from math import ceil

N,M,K,Q = map(int, input().split())
cans = [[int(i) for i in input().split()] for j in range(N)]
cans.sort(key = lambda x: (x[0], x[1]))
mc = sum([i[0] for i in cans[:M]])
tc = sum([i[1] for i in cans[:M]])
canm = [i[0] for i in cans[M:] if i[1] == 0][::-1]
mcan = [i[0] for i in cans[:M] if i[1] == 1]
# print(cans[:M])
mincost = mc + ceil(len(mcan) / K)*Q
for i in range(min(len(mcan),len(canm))):
    # print(canm, mcan)
    mcc = mc + ceil(len(mcan) / K)*Q
    mcp = (mc - mcan[-1] + canm[-1]) + ceil((len(mcan)-1) / K)*Q
    cp = canm.pop()
    cm = mcan.pop()

    # print(mcc, mcp, ceil(len(mcan) / K))
    if mcp < mincost:
        mincost = mcp
    mc += cp - cm
print(mincost)