from math import factorial
from collections import Counter
n,k = [int(i) for i in input().split()]
s = input()
w = input().split()
s = [i for i in s if i in w]
print(s)
c = Counter(s)
t = 1
for a in c.values():
    t *= a
print(len(s)*(len(s)+1)//2//t)