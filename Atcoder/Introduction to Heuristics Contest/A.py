D = int(input())
C = [int(i) for i in input().split()]
scores = [[int(i) for i in input().split()] for j in range(D)]
ans = [0]*D
S = 0
last = [0]*26
for d in range(1,D+1):
    m = -float("inf")
    index = -1
    for i,t in enumerate(scores[d-1]):
        st = S + t
        lt = [i for i in last]
        lt[i] = d
        for j in range(26):
            st -= C[j] * (d - lt[j])
        if m < st:
            m = st
            index = i
    S = m
    ans[d-1] = index+1
    last[index] = d
print("\n".join(map(str, ans)))

# from time import time
#
# start = time()
# D = int(input())
# C = [int(i) for i in input().split()]
# scores = [[int(i) for i in input().split()] for j in range(D)]
# t = []
# for i in scores:
#     t.append(i.index(max(i))+1)
# DC = [0]*26
#
# def calcScore(t):
#     score = []
#     S = 0
#     last = [0]*26
#     for d in range(1,D+1):
#         S += scores[d-1][t[d-1]-1]
#         last[t[d-1]-1] = d
#         for i in range(26):
#             S -= C[i] * (d - last[i])
#             DC[i] += (d - last[i])
#         score.append(S)
#     return score[-1]
#
# ts = calcScore(t)
# i = D
# j = 1
# m = 1
# while time() - start < 1.95:
#     d,q = i, j
#     temp = [t[i] if d-1 != i else q for i in range(D)]
#     j += m
#     if calcScore(temp) > ts:
#         t = temp
#         i -= 1
#         j = 0
#         if i < 0:
#             i = D//2
#
# print("\n".join(map(str, t)))



# from time import time
#
# start = time()
# D = int(input())
# C = [int(i) for i in input().split()]
# scores = [[int(i) for i in input().split()] for j in range(D)]
# t = []
# for i in scores:
#     t.append(i.index(max(i))+1)
# DC = [0]*26
#
# def calcScore(t):
#     score = []
#     S = 0
#     last = [0]*26
#     for d in range(1,D+1):
#         S += scores[d-1][t[d-1]-1]
#         last[t[d-1]-1] = d
#         for i in range(26):
#             S -= C[i] * (d - last[i])
#             DC[i] += (d - last[i])
#         score.append(S)
#     return score[-1]
#
# ts = calcScore(t)
# i = D
# j = 1
# while time() - start < 1.95:
#     d,q = i, j
#     temp = [t[i] if d-1 != i else q for i in range(D)]
#     j += 1
#     if calcScore(temp) > ts:
#         t = temp
#         i -= 1
#         j = 0
#
# print("\n".join(map(str, t)))