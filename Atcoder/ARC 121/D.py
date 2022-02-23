from collections import deque

N = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
da = deque(a)
sa = sum(a)
aa = sa / len(a)
print(a)
print(sa, aa)