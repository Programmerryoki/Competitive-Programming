from sys import stdin
from math import ceil
from collections import defaultdict

def main():
    input = stdin.readline
    n,m = map(int, input().split())
    ph = [float(input()) for i in range(n)]
    ans = []
    for _ in range(m):
        start, end = map(int, input().split())
        mid = ceil((end - start) / 2)
        phs = [[0,defaultdict(int)] for i in range(15)]
        for p in ph[start-1:end]:
            phs[int(p // 1)][0] += 1
            phs[int(p // 1)][1][p] += 1
        num = -1
        for i in range(len(phs)):
            if phs[i][0] > mid:
                num = i
                break
        if num < 0:
            ans.append("unusable")
            continue
        arr = phs[num][1]
        for i in arr:
            if arr[i] > mid:
                ans.append("usable")
                break
        else:
            ans.append("unusable")
    print("\n".join(ans))

if __name__ == "__main__":
    main()