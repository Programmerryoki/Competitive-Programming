from math import ceil

N = int(input())
A = [int(i) for i in input().split()]
n = [0]*N
for a in A:
    n[a] += 1
# print(n)
if N&1:
    t = 0
    for a in range(len(n)):
        if a == 0:
            if n[a] != 1:
                print(0)
                break
        elif a&1:
            if n[a] != 0:
                print(0)
                break
        else:
            if n[a] != 2:
                print(0)
                break
            else:
                t += 1
    else:
        print(2**t%(10**9+7))
else:
    t = 0
    for a in range(len(n)):
        if a&1:
            if n[a] != 2:
                print(0)
                break
            else:
                t += 1
        else:
            if n[a] != 0:
                print(0)
                break
    else:
        print(2**t%(10**9+7))