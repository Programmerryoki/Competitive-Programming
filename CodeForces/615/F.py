import heapq


def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b = [int(i) for i in input().split()]
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)

    m = tree.index(max(tree, key = len))
    que = [] + tree[m]
    dep = [-1]*n
    dep[m] = 0
    num = n-1
    d = 0
    while num != 0:
        nque = []
        d += 1
        while len(que) != 0:
            s = que.pop()
            if dep[s] == -1:
                dep[s] = d
                num -= 1
            nque += tree[s]
        que = list(set(nque))
    ma = max(dep)
    ans = heapq.nlargest(3, range(len(dep)), key=dep.__getitem__)
    pos = [[ans[0],ans[1]],[ans[0],ans[2]],[ans[1],ans[2]]]
    ma = 0
    for a,b in pos:
        print(a,b)
        d = 1
        que = [] + tree[a]
        nque = []
        found = False
        seen = [a]
        while not found:
            while len(que) != 0:
                s = que.pop()
                if s not in seen:
                    seen.append(s)
                    if b in tree[s]:
                        found = True
                        break
                    else:
                        nque += tree[s]
            else:
                que = list(set(nque))
            d += 1
        if d > ma:
            ma = d
    print(ma)

    for a in range(len(ans)):
        ans[a] += 1
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()