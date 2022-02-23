from sys import setrecursionlimit, stdin
setrecursionlimit(10**8)

def main():
    input = stdin.readline
    N = int(input())
    C = [int(i) for i in input().split()]
    graph = {i:set() for i in range(N)}
    for _ in range(N-1):
        A,B = map(lambda x: int(x)-1, input().split())
        graph[A].add(B)
        graph[B].add(A)

    ans = []
    def dfs(current : int, color : set, sen : set):
        if C[current] not in color:
            ans.append(current+1)
        for node in graph[current]:
            if node not in sen:
                sen.add(current)
                rem = (C[current] in color)
                color.add(C[current])
                dfs(node, color, sen)
                if not rem:
                    color.remove(C[current])
                sen.remove(current)

    dfs(0, set(), set())
    ans.sort()
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()