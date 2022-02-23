import sys
import math


def shellSort(A, n):
    global cnt
    cnt = 0
    m = n//5+1
    G = []
    for a in range(1,n,m):
        G.insert(0, a)
    # print(m,G)
    print(len(G))
    print(" ".join(map(str, G)))
    for i in range(m):
        # print(A)
        insertionSort(A, n, G[i])


def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i-g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j-g
            cnt += 1
            # print("\t",A)
        A[j+g] = v
        # print("\t",A)


def main():
    input = sys.stdin.readline
    n = int(input())
    A = [int(input()) for i in range(n)]
    shellSort(A, n)
    # print(A)
    print(cnt)
    for a in A:
        print(a)


if __name__ == "__main__":
    main()