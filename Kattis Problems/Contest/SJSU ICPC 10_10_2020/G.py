from copy import deepcopy
from sys import stdin, getsizeof

def main():
    input = stdin.readline
    n,m = map(int, input().split())
    ph = [float(input()) for i in range(n)]
    sph = list(set(ph))
    nn = [0]*len(sph)
    dic = [0]*(n+1)
    dic[0] = nn
    for i in range(n):
        t = deepcopy(dic[i])
        t[sph.index(ph[i])] += 1
        dic[i+1] = t

    ans = [""] * m
    for i in range(m):
        l,r = map(int, input().split())
        d = [dic[r][i] - dic[l-1][i] for i in range(len(sph))]
        ans[i] = "usable" if max(d) >= (r-l+1)//2 + 1 else "unusable"
        print(max(d))
    print("\n".join(ans))

if __name__ == "__main__":
    main()

# from copy import deepcopy
# from collections import Counter
# from sys import stdin
#
# def main():
#     input = stdin.readline
#     n,m = map(int, input().split())
#     ph = [float(input()) for i in range(n)]
#     dic = [""] * (n + 1)
#     dic[0] = Counter()
#     for i in range(n):
#         t = deepcopy(dic[i])
#         t.setdefault(ph[i], 0)
#         t[ph[i]] += 1
#         dic[i+1] = t
#
#     ans = [""] * m
#     for i in range(m):
#         l,r = map(int, input().split())
#         d = dic[r] - dic[l-1]
#         ans[i] = "usable" if d.most_common(1)[0][1] >= (r-l+1)//2 + 1 else "unusable"
#     print("\n".join(ans))
#
# if __name__ == "__main__":
#     main()