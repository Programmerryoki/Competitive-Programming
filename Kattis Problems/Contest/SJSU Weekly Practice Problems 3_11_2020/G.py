from itertools import accumulate

T = int(input())
for _ in range(T):
    N = int(input())
    t = []
    for a in range(N):
        t.append(sum([int(i) for i in input().split()[1:]]))
    t.sort()
    at = sum(accumulate(t))/len(t)
    print(at)