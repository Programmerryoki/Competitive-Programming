t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    adding = 0
    ma = -float("inf")
    for i in A:
        if i + adding > ma:
            ma = i + adding
        adding -= (adding + i)
    print(ma)