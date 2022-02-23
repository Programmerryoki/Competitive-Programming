import datetime
a = datetime.date(2019,6,29)
b = datetime.date(2019,6,30)
d = str(b-a)
print(d[:d.index(" ")])
# from itertools import accumulate
# N, P = [int(i) for i in input().split()]
# ns = [int(i)-20 for i in input().split()]
# an = list(accumulate(ns))
# ma = 0
# for i,a in enumerate(an):
#     for j,b in enumerate(an[i+1:]):
#         if b-a > ma:
#             ma = b-a
# print(ma)