from sys import stdin
from collections import deque

def main():
    input = stdin.readline
    N = int(input())
    graph = {i:set() for i in range(1,N+1)}
    for _ in range(N-1):
        u,v = [int(i) for i in input().split()]
        graph[u].add(v)
        graph[v].add(u)
    for i in range(1,N):
        if len(graph[i]) > 1:
            break
    leafs = deque()
    seen = {i}
    que = deque([i])
    while que:
        cur = que.popleft()
        leaf = True
        for nxt in graph[cur]:
            if nxt not in seen:
                leaf = False
                que.append(nxt)
                seen.add(nxt)
        if leaf:
            leafs.append(cur)

    total = len(leafs)
    nums = [-1] * N
    for i in leafs:
        nums[i-1] = 1
    seen = set(leafs)
    while leafs:
        print(leafs)
        print(nums, seen)
        cur = leafs.popleft()
        t = 0
        for nxt in graph[cur]:
            if nxt not in seen:
                leafs.append(nxt)
                seen.add(nxt)
            else:
                t += nums[nxt-1]
        if not nums[cur-1]:
            nums[cur-1] = t
            total += t
    print(total)


if __name__ == '__main__':
    main()