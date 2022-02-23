from sys import stdin

def main():
    input = stdin.readline
    T = int(input())
    for case in range(T):
        N,M,K = [int(i) for i in input().split()]
        rooms = [[int(i) for i in input().split()] for _ in range(N)]
        graph = {i:set() for i in range(N)}
        for _ in range(M):
            x,y = [int(i) for i in input().split()]
            graph[x].add(y)
            graph[y].add(x)

        count = 0
        seen = set()
        inque = set()
        parent = []
        def dfs(room, mp):
            nonlocal count, seen, inque, parent
            if mp == K:
                count += 1
                return
            elif mp > K:
                return
            c = 0
            for nxt in graph[room]:
                if nxt in inque or nxt in seen:
                    continue
                c += 1
                parent.append(nxt)
                inque.add(nxt)
            for i in parent:
                if i in seen:
                    continue
                L,R,A = rooms[i]
                if L <= mp <= R:
                    seen.add(i)
                    dfs(i, mp+A)
                    seen.remove(i)
            for i in range(c):
                inque.remove(parent.pop())


        for i in range(N):
            seen.clear(); inque.clear(); parent.clear()
            seen.add(i)
            dfs(i, rooms[i][-1])
        print(f"Case #{case+1}: {count}")


if __name__ == '__main__':
    main()