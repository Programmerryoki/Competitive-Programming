# import psutil
# import os
from functools import reduce

n = int(input())
num = [int(i) for i in input().split()]
sm = [0]*(n+1)
for i in range(n):
    sm[i+1] = num[i] + sm[i]
try:
    last1 = len(num) - num[::-1].index(1)
except:
    last1 = 0
c = 0
for i in range(n):
    mm = num[i]
    for j in range(i+2, n+1):
        mm *= num[j-1]
        sn = sm[j] - sm[i]
        if sn == mm:
            c += 1
        if mm > sn and j > last1:
            break
print(c)

# process = psutil.Process(os.getpid())
# print(process.memory_info().rss / float(2 ** 20))