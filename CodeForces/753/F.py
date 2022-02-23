from sys import stdin

def main():
    moves = {"L":(0,-1),"R":(0,1),"D":(1,0),"U":(-1,0)}
    input = stdin.readline
    t = int(input())
    for _ in range(t):
        input()
        n,m = [int(i) for i in input().split()]
        commands = [input() for _ in range(n)]
        graph = {}
        for i in range(1,n+1):
            for j in range(1,m+1):
                dx,dy = moves[commands[i-1][j-1]]
                nxt = (i+dx,j+dy)
                if 1<=nxt[0]<=n and 1<=nxt[1]<=m:
                    graph[(i,j)] = nxt
        longest = {}
        long = 0
        start = None
        for i in range(1,n+1):
            for j in range(1,m+1):
                if (i,j) in longest:
                    continue
                cur = (i,j)
                order = []
                seen = set()
                while True:
                    if cur in seen or cur in longest:
                        break
                    order.append(cur)
                    if cur not in graph:
                        break
                    seen.add(cur)
                    cur = graph[cur]
                cycle = cur in seen
                ec = cur
                ori = {}
                d = 1 if cycle or cur not in graph else longest[cur]+1
                for pos in order[::-1]:
                    if cycle:
                        ori[pos] = d
                        if pos == ec:
                            cycle = False
                        d += 1
                    else:
                        longest[pos] = d
                        d += 1
                if (i,j) in longest and longest[(i,j)] > long:
                    long = longest[(i,j)]
                    start = (i,j)
                if (i,j) in ori and ori[(i,j)] > long:
                    long = ori[(i,j)]
                    start = (i,j)
        print(start[0],start[1],long)


if __name__ == '__main__':
    main()