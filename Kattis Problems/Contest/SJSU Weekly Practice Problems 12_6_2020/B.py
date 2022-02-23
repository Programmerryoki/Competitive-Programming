from bisect import bisect_right, bisect_left

T = int(input())
for _ in range(T):
    input()
    NCS, NE = map(int, input().split())
    ncs = [int(i) for i in input().split()]
    ne = [int(i) for i in input().split()]
    ancs = sum(ncs) / NCS
    ane = sum(ne) / NE
    ncs.sort()
    ne.sort()
    i = bisect_left(ncs, ancs)
    j = bisect_right(ncs, ane)
    # print(ncs)
    # print(ancs,i, ane,j)
    print(max(0, i - j))