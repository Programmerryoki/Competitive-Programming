numset = set("012")
t = int(input())
for _ in range(t):
    n = int(input())
    s = input() + " "
    t = input() + " "
    cv = 0
    ps = set()
    pv = 0
    for i in range(n):
        stmp = {s[i],t[i]}
        v1 = int(min(numset - stmp))
        v2 = int(min(numset - ps - stmp))
        # print(i,cv,stmp,ps,numset - ps - stmp, v1,v2,pv)
        if v2 > pv + v1:
            cv += v2
            pv = 0
            ps.clear()
        elif v2 == 2:
            cv += pv
            pv = v1
            ps = stmp
        elif v1 < v2:
            pv = v2
            ps |= stmp
        elif v1 >= v2:
            cv += pv
            pv = v1
            ps = stmp
    cv += int(min(numset - ps))
    print(cv)