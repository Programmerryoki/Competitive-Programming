from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)


def main():
    input = stdin.readline
    ts = lambda x: 0 if not len(x) else sum([x[i] / (2**i) for i in range(len(x))])

    n,m = map(int, input().split())
    c = [int(i) for i in input().split()]
    graph = {i:set() for i in range(n)}
    for _ in range(m):
        s,t = map(int, input().split())
        graph[s].add(t)

    que = deque([[0, [c[0]]]])
    seen = {0}
    ms = 0
    while que:
        cp, sat = que.popleft()
        end = True
        for stall in graph[cp]:
            if stall not in seen:
                end = False
                que.append([stall, sat + [c[stall]]])
        seen.add(cp)
        if end:
            for i in range(2**len(sat)):
                bn = bin(i)[2:]; bn = "0"*(len(sat)-len(bn)) + bn
                tmp = ts([sat[j] for j in range(len(sat)) if bn[j] == "1"])
                if tmp > ms:
                    ms = tmp
    print(ms)

if __name__ == "__main__":
    main()