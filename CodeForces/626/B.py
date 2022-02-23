n,m,k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

# for i in a:
#     for j in b:
#         print(str(i*j)+" ",end = "")
#     print()

ps = []
for i in range(1,k+1):
    if k%i==0:
        ps.append([i,k//i])
blcs = [[],[]]
ind = -1
for i,e in enumerate(a):
    if e == 0:
        blcs[0].append(i-ind-1)
        ind = i
if ind != n-1:
    if ind == 0:
        blcs[0].append(n)
    else:
        blcs[0].append(n-ind-1)
ind = -1
for j,e in enumerate(b):
    if e == 0:
        blcs[1].append(j-ind-1)
        ind = j
if ind != m-1:
    if ind == 0:
        blcs[1].append(m)
    else:
        blcs[1].append(m-ind-1)
# print(blcs)
count = 0
for p in ps:
    for i in blcs[0]:
        for j in blcs[1]:
            count += max(i-p[0]+1,0)*max(j-p[1]+1,0)
print(count)

# n,m,k = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
# ps = []
# for i in range(1,k+1):
#     if k%i==0:
#         ps.append([i,k//i])
#
# count = 0
# for p in ps:
#     for aa in range(n-p[0]+1):
#         for bb in range(m-p[1]+1):
#             if 0 not in a[aa:aa+p[0]] + b[bb:bb+p[1]]:
#                 count += 1
# print(count)