from sys import stdin
from heapq import heappush, heappop, nlargest
from bisect import insort_left
from collections import deque

def main():
    input = stdin.readline
    T = int(input())
    for case in range(T):
        D,N,K = [int(i) for i in input().split()]
        att = [[int(i) for i in input().split()] for _ in range(N)]
        att.sort(key=lambda x: (x[1], x[2], x[0]))
        pos = []
        j = 0
        mh = 0
        for i in range(1, D+1):
            while j < N and att[j][1] == i:
                heappush(pos, (att[j][2],att[j][0]))
                j += 1
            while pos and pos[0][0] < i:
                heappop(pos)
            h = sum(i[1] for i in nlargest(K, pos, key=lambda x: (x[1])))
            if h > mh:
                mh = h
        print(f"Case #{case+1}: {mh}")


if __name__ == '__main__':
    main()