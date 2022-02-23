from sys import stdin
from bisect import bisect_left

def main():
    input = stdin.readline

    n = int(input())
    lst = []
    t = 0
    for _ in range(n):
        a = int(input())
        index = bisect_left(lst, a)
        t += len(lst) - index
        lst.insert(index, a)
    print(t)


if __name__ == "__main__":
    main()