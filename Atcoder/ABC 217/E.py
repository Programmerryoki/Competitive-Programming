from collections import deque
from sys import stdin

def main():
    input = stdin.readline
    Q = int(input())
    arr = deque()
    ans = []
    for _ in range(Q):
        c,*rest = [int(i) for i in input().split()]
        if c == 1:
            x = rest[0]
            arr.append(x)
        elif c == 2:
            ans.append(str(arr.popleft()))
        else:
            arr = deque(sorted(arr))
    print("\n".join(ans))

if __name__ == '__main__':
    main()