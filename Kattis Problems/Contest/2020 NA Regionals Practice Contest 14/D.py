from sys import setrecursionlimit
setrecursionlimit(10**8)

def main():
    n,w = map(int, input().split())
    dams = [[int(i) for i in input().split()] for j in range(n)]
    graph = {i:set() for i in range(n+1)}
    for i,[d,c,u] in enumerate(dams):
        graph[d].add(i+1)
    # print(graph)
    def dfs(current):
        if current == 0:
            cd = [-1, w, 0]
            dif = w
        else:
            cd = dams[current-1]
            dif = cd[1] - cd[2]
        rset = set()
        for node in graph[current]:
            S = dfs(node)
            for wa in S:
                if wa[1] >= dif:
                    t = wa[1] + cd[2]
                    rset.add((wa[0], t))
        rset.add((dif, cd[1]))
        return rset
    anss = dfs(0)
    # print(anss)
    ans = list(anss)
    ans.sort()
    for mw, gw in ans:
        if gw >= w:
            print(mw)
            break

if __name__ == "__main__":
    main()