t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    m = -float("INF")
    op = 1
    if A[0] < 0:
        op = -1

    ans = 0
    for i in A:
        if op == 1:
            if i > 0:
                if i > m:
                    m = i
            else:
                ans += m
                m = i
                op = -1
        else:
            if i < 0:
                if i > m:
                    m = i
            else:
                ans += m
                m = i
                op = 1
    ans += m
    print(ans)