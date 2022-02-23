from itertools import permutations

def main():
    N = int(input())
    A = [[int(i) for i in input().split()] for j in range(N)]
    M = int(input())
    bad = {i:set() for i in range(N)}
    for _ in range(M):
        X,Y = [int(i)-1 for i in input().split()]
        bad[X].add(Y)
        bad[Y].add(X)

    mint = float("inf")
    for per in permutations([i for i in range(N)], N):
        for i in range(len(per)-1):
            if per[i+1] in bad[per[i]]:
                break
        else:
            time = sum([A[per[i]][i] for i in range(N)])
            if time < mint:
                mint = time
    print(mint if mint != float("inf") else -1)


    # graph = {j:set([i for i in range(N)]) for j in range(N)}
    # for _ in range(M):
    #     X,Y = [int(i)-1 for i in input().split()]
    #     graph[X].remove(Y)
    #     graph[Y].remove(X)
    # graph[-1] = set([i for i in range(N)])
    # A += [[0]*N]
    #
    # mint = float("inf")
    # used = set()
    # def recur(prev, cur, t):
    #     # print(prev,cur,t, used)
    #     nonlocal mint
    #     if cur == N:
    #         if t < mint:
    #             mint = t
    #         return
    #     for p in graph[prev]:
    #         if p not in used:
    #             used.add(p)
    #             recur(p, cur + 1, t + A[p][cur])
    #             used.remove(p)
    #
    # recur(-1, 0, 0)
    # print(mint if mint != float("inf") else -1)

if __name__ == '__main__':
    main()