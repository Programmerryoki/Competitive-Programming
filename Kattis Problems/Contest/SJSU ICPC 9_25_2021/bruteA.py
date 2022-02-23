def serialize(start, end):
    return ",".join(map(str, sorted(start)))+";"+",".join(map(str, sorted(end)))

N,*times = [int(i) for i in input().split()]

mt = float("inf")
seen = set()
def dfs(start, end, cloth, time):
    global mt, seen
    if len(end) == N:
        mt = min(mt, time)
        return
    ser = serialize(start, end)
    if ser in seen:
        return
    seen.add(ser)
    print(start,end)
    if cloth:
        for i in range(N):
            if i not in start:
                continue
            for j in range(i+1, N):
                if j not in start:
                    continue
                start.remove(i)
                start.remove(j)
                end.add(i)
                end.add(j)
                dfs(start,end,0,time + max(times[i], times[j]))
                start.add(i)
                start.add(j)
                end.remove(i)
                end.remove(j)
    else:
        m = min(end)
        end.remove(m)
        start.add(m)
        dfs(start, end, 1, time + times[m])

dfs(set([i for i in range(N)]), set(), 0)
print(mt)