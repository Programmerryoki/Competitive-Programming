from bisect import bisect_left

n = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]
n = 0
for t in T:
    index = bisect_left(S, t)
    if index < len(S) and S[index] == t:
        n += 1
print(n)