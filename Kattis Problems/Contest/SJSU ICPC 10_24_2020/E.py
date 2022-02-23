from bisect import bisect_left

n,m = map(int, input().split())
size = list(set([int(input()) for i in range(n)]))
buy = [int(input()) for i in range(m)]
size.sort()
tw = 0
for i in buy:
    tw += size[bisect_left(size, i)] - i
print(tw)