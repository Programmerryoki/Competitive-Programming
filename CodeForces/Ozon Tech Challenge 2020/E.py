n, m = [int(i) for i in input().split()]
pos = True
if n > 2:
    # maximum = n * (n-1) * (n-2) // 6
    # if maximum < m:
    #     print(-1)
    #     pos = False
    if n - 2 < m:
        print(-1)
        pos = False
if pos:
    ans = [1,2]
    for i in range(m):
        ans.append(ans[i]+ans[i+1])
    for i in range(n - len(ans)):
        ans.append(ans[-1]+ans[-2]+1)
    print(" ".join(map(str, ans[:n])))