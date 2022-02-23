from collections import Counter
from itertools import takewhile


def intersect(a,b):
    if int(a[0]) <= int(b[0]) <= int(a[1]):
        return True
    if int(a[0]) <= int(b[1]) <= int(a[1]):
        return True
    return False


t = int(input())
for _ in range(t):
    n = int(input())
    seg = [input() for i in range(n)]
    count = Counter(seg)
    vals = [x for x, _ in takewhile(lambda x: x[1]==1, count.most_common()[::-1])]
    for a in range(len(vals)):
        