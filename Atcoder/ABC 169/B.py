from functools import reduce
N = int(input())
A = [int(i) for i in input().split()]
A.sort(reverse=True)
if A[-1] == 0:
    print(0)
else:
    s = 1
    for a in A:
        s *= a
        if s == 0:
            print(0)
            break
        if s > 10**18:
            print(-1)
            break
    else:
        print(s)