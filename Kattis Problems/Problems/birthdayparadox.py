import math
from collections import Counter

##########
# PLAN A #
##########
# n = int(input())
# cs = [int(i) for i in input().split()]
# scs = sum(cs)
#
# basic = math.factorial(365)/(math.factorial(n) * math.factorial(365 - n))
# c1 = 1
# for a in cs:
#     c1 *= math.factorial(a)
# print(c1)
# comb = math.factorial(scs)/(c1)
# csc = Counter(cs)
# c2 = 1
# for a in csc.values():
#     c2 *= math.factorial(a)
# final = math.factorial(n) / (c2)
#
# ans = basic * comb * final / (365 ** scs)
# print(math.log10(ans))


##########
# PLAN B #
##########
n = int(input())
cs = [int(i) for i in input().split()]
scs = sum(cs)

top = [0 for i in range(max(366,scs+1))]
bot = [0 for i in range(max(366,scs+1))]

def mulB(n):
    for num in range(1,n+1):
        if bot[num] >= 1:
            bot[num] -= 1
        else:
            top[num] += 1

def divB(n):
    for num in range(1,n+1):
        if top[num] >= 1:
            top[num] -= 1
        else:
            bot[num] += 1

bot[365] += scs
mulB(365)
divB(n)
divB(365 - n)
mulB(scs)
for a in cs:
    if a != 1:
        divB(a)
mulB(n)
csc = Counter(cs)
for a in csc.values():
    divB(a)
# print(top)
# print(bot)
ct = 0
cb = 0
for a in range(1,len(top)):
    # print(a,c)
    if top[a] != 0:
        ct += math.log10(a**top[a])
    if bot[a] != 0:
        cb += math.log10(a**bot[a])
print(ct - cb)

##########
# PLAN C #
##########
# n = int(input())
# cs = [int(i) for i in input().split()]
# scs = sum(cs)
#
# count = [0 for i in range(366)]
#
# def mulB(n,d):
#     for num in range(1,n+1):
#        count[num] += 1
#
# def divB(n):
#     for num in range(1,n+1):
#        count[num] -= 1
#
# mulB(365)
# divB(n)
# divB(365 - n)
#
#
# print(count)