N = int(input())
pers = []
names = []
modi = [1]*N
temp = 100
for i in range(N):
    name, per = input().split()
    names.append(name)
    if per != "?":
        temp -= int(per)
        pers.append([int(per),int(per)])
        modi[i] = 0
    else:
        pers.append([float("inf"),-1])
pers = pers[::-1]
modi = modi[::-1]
# print(pers)

def mibfs(ps, i, prev, left):
    # print(ps, i, prev,left)
    if i == len(ps):
        global pers
        if left != 0:
            return
        # print(ps)
        for i in range(N):
            pers[i] = [min(pers[i][0], ps[i]), max(pers[i][1], ps[i])]
        raise ImportError

    if ps[i] == float("inf"):
        tmp = [i for i in ps]
        for t in range(prev, min(left+1, ps[i+1]+1 if i != N-1 else float('inf'))):
            tmp[i] = t
            mibfs(tmp, i+1, t, left - t)
    else:
        mibfs(ps, i+1, ps[i], left)

def mabfs(ps, i, prev, left):
    # print(ps, i, prev,left)
    if i == len(ps):
        global pers
        if left != 0:
            return
        # print(ps)
        for i in range(N):
            if modi[i]:
                pers[i] = [min(pers[i][0], ps[i]), max(pers[i][1], ps[i])]
        # raise ImportError

    if ps[i] == float("inf"):
        tmp = [i for i in ps]
        for t in range(min(left, ps[i+1] if i != N-1 else float('inf')), prev-1,-1):
            tmp[i] = t
            mabfs(tmp, i+1, t, left - t)
    else:
        mabfs(ps, i+1, ps[i], left)

cp = [[i for i in j] for j in pers]

try:
    mibfs([i[0] for i in cp], 0, 0, temp)
except:
    pass

try:
    mabfs([i[0] for i in cp], 0, 0, temp)
except:
    pass

print("\n".join([" ".join(map(str,[names[i]]+pers[N-i-1])) for i in range(N)]))