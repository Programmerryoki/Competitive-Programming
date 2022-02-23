from sys import stdin
from heapq import heappush, heappop

def main():
    input = stdin.readline
    n, C = [int(i) for i in input().split()]
    users = [[int(i) for i in input().split()] for _ in range(n)]
    users.sort(key=lambda x: (x[1],x[0],x[2]))
    heap = []
    for i in range():


if __name__ == '__main__':
    main()