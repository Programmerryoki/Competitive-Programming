from collections import deque
from sys import stdin

def main():
    input = stdin.readline
    n,k = map(int, input().split())
    nodes = [int(input(), 2) for i in range(n)]
    que = deque(nodes)
    seen = [-1]*(2**k)
    for i in nodes:
        seen[i] = 0
    while que:
        node = que.popleft()
        mask = 1
        for i in range(k):
            n = node ^ mask
            if seen[n] == -1:
                seen[n] = seen[node] + 1
                que.append(n)
            mask <<= 1
    ans = bin(seen.index(max(seen)))[2:]
    print("0"*(k - len(ans)) + ans)

if __name__ == "__main__":
    main()