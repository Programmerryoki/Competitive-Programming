from collections import defaultdict, Counter

n = int(input())
a = [int(i) for i in input().split()]
ac = Counter(a)
aci = list(ac.keys())
count = defaultdict(int)
for i in range(len(aci)):
    for j in range(i+1,len(aci)):
        num = aci[i]+aci[j]
        count[num] += ac[aci[i]]*ac[aci[j]]

s = 0
for i in count.keys():
    if count[i]%2==1:
        s ^= i
print(s)

# from collections import defaultdict
#
# n = int(input())
# a = [int(i) for i in input().split()]
# count = defaultdict(int)
# for i in range(n):
#     for j in range(i+1,n):
#         count[a[i]+a[j]] += 1
# s = 0
# for i in count.keys():
#     if count[i]%2==1:
#         s ^= i
# print(s)