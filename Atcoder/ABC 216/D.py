from sys import stdin


def main():
    input = stdin.readline
    N,M = [int(i) for i in input().split()]
    graph = {i:set() for i in range(N)}
    rgraph = {i:set() for i in range(N)}
    for _ in range(M):
        k = int(input())
        A = [int(i)-1 for i in input().split()]
        for i in range(k-1):
            graph[A[i]].add(A[i+1])
            rgraph[A[i+1]].add(A[i])

    order = []
    seen = set()
    for i in range(N):
        if i in seen:
            continue
        seen.add(i)
        que = [i]
        o = []
        while que:
            node = que.pop()
            o.append(node)
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    que.append(n)
        order += o[::-1]
    print(rgraph)
    print(order)
    seen.clear()
    rank = {order[i]:i for i in range(N)}
    print(rank)
    for i in range(N-1,-1,-1):
        seen.add(order[i])
        print(i, order[i])
        for r in rgraph[order[i]]:
            if r not in seen and rank[r] < rank[order[i]]:
                print("No")
                exit()
    print("Yes")


if __name__ == '__main__':
    main()