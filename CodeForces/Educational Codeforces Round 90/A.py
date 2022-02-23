T = int(input())
for _ in range(T):
    a,b,c = [int(i) for i in input().split()]
    ans = [-1,-1]
    if a > c:
        ans[0] = -1
        ans[1] = 1
    elif a < c:
        ans[0] = 1
        if a*b > c:
            ans[1] = b
        else:
            ans[1] = -1
    else:
        ans[0] = -1
        ans[1] = 2

    print(" ".join(map(str, ans)))