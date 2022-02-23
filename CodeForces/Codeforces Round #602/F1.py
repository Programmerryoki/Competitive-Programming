# def diff(h, hr):
#     return sum([1 if h[i] != hr[i] else 0 for i in range(len(h))])

n, k = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
hr = [h[-1]] + h[:-1]
###################################
# nums = [i for i in range(1,k+1)]
# que = []
# pos = nums.copy()
# for a in range(n-1):
#     que.extend(pos)
#     pos = []
#     for b in que:
#         for c in nums:
#             pos.append(int(str(b) + str(c)))
#     que = []
# print(pos)
# hs = "".join(list(map(str, h)))
# hrs = "".join(list(map(str, hr)))
# c = 0
# for a in pos:
#     if diff(str(a), hs) > diff(str(a), hrs):
#         print(a)
#         c += 1
# print(c)
#####################################
print(h)
print(hr)
c = sum([1 if h[i] != hr[i] else 0 for i in range(len(h))])

cl = [k if h[i] != hr[i] else k-1 for i in range(len(h))]
total = 1
for a in cl:
    total *= a
print((total//2)%998244353)