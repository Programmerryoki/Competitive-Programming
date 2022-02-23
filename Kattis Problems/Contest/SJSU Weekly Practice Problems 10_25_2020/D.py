from math import gcd

P = int(input())
ans = []
for _ in range(P):
    K,N = map(int, input().split())
    n = 2
    for a in range(1,N-1):
        for b in range(a+1,N):
            if gcd(a,b) == 1:
                n += 1
    ans.append(n)
print("\n".join(map(str, ans)))

# from math import gcd
#
# P = int(input())
# ans = []
# for _ in range(P):
#     K,N = [int(i) for i in input().split()]
#     sfs = set()
#     for b in range(1,N+1):
#         for a in range(b):
#             n = gcd(a,b)
#             if n != 1:
#                 continue
#             sfs.add(a / b)
#     ans.append([K, len(sfs)])
# print("\n".join(" ".join(map(str, i)) for i in ans))