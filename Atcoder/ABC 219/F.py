def main():
    S = input()
    K = int(input())
    moves = {"U":(0,-1),"D":(0,1),"R":(1,0),"L":(-1,0)}
    cur = [0,0]
    seen = {(0,0)}
    check = set()
    for s in S:
        cur[0] += moves[s][0]
        cur[1] += moves[s][1]
        t = (cur[0], cur[1])
        if t not in seen:
            seen.add(t)
            check.add(t)
    end = t
    steps = []
    p = 0
    while len(steps) < K:
        rem = set()
        for ch in check:
            t = (cur[0]+ch[0], cur[1]+ch[1])
            if t not in seen:
                seen.add(t)
            else:
                rem.add(ch)
        for i in rem:
            check.remove(i)
        m = len(seen) - p
        if steps and steps[-1] == m:
            break
        steps.append(m)
        p = len(seen)
        cur[0] += end[0]
        cur[1] += end[1]
    if len(steps) >= K:
        print(sum(steps[:K]))
    else:
        print(steps[-1] * (K-len(steps)) + sum(steps[:-1]))


if __name__ == '__main__':
    main()