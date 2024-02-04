def recur(num):
    n = 4
    ans = ""
    d = 10
    for _ in range(5000):
        ans += str(d//num)
        d -= num*(d//num)
        if d == 0:
            break
        d *= 10

        for j in range(len(ans)//2+1):
            la = len(ans) - j
            # print(la//n, ans[j:j+la//n],ans[j+la//n:j+la//n*2],ans[j+la//n*2:j+la//n*3],ans[j+la//n*3:j+la//n*4])
            if ans[j:j+la//n] == ans[j+la//n:j+la//n*2] and ans[j+la//n*2:j+la//n*3] == ans[j+la//n*3:j+la//n*4]:
                if not ans[j:j+la//n] or int(ans[j:j+la//n]) == 0:
                    continue
                return ans[:j + la // n], la // n
    return ans, len(ans)

ml = 0
l = ""
for d in range(2,1000):
    a = recur(d)
    # print(d, "0." + a[0], a[1])
    if a[1] > ml:
        ml = a[1]
        l = a[0]
        print(d, ml, "0."+l)