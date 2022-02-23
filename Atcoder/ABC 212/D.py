from heapq import heappush, heappop
from sys import stdin

def main():
    input = stdin.readline
    Q = int(input())
    heap = []
    adding = [0]
    for _ in range(Q):
        # print(heap, adding)
        P, *X = [int(i) for i in input().split()]
        if P == 1:
            X = X[0]
            heappush(heap, [X-adding[-1], len(adding)-1])
        elif P == 2:
            X = X[0]
            adding.append(adding[-1]+X)
        else:
            v,ad = heappop(heap)
            print(v + adding[-1])

if __name__ == '__main__':
    main()