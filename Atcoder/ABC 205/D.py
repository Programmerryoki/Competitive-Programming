from sys import stdin
from bisect import bisect_left, bisect_right

def main():
    input = stdin.readline
    N,Q = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    ans = [0]*Q
    for i in range(Q):
        K = int(input())
        tmp = bisect_right(A, K)
        t = K + tmp
        # print(tmp, t)
        while True:
            # print(tmp, t)
            ind = bisect_right(A, t)
            if ind == tmp:
                break
            t += ind - tmp
            tmp = ind
        ans[i] = t

        # for j in range(N):
        #     if t + j == A[tmp+j]:
        #         continue
        #     else:
        #         break
        # t += j
        # ans[i] = t
    print()
    print("\n".join([str(i) for i in ans]))

if __name__ == '__main__':
    main()