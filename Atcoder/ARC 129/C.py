N = int(input())
ans = []
while N > 0:
    i = 0
    while (i+2)*(i+1) <= 2*N:
        i += 1
    N -= (i+1)*i // 2
    ans.append("7"*i)
tmp = ""
n = 0
pv = ["0"]
for i in ans[:-1]:
    n = int(str(n)+i) % 7
    for t in range(1,7):
        for p in pv:
            if (n*10+t)%7==0 or int(p+i+str(t))%7==0:
                break
        else:
            break
    else:
        break
    tmp += i + str(t)
    n = (n * 10 + t) % 7
    for p in range(len(pv)):
        pv[p] += i+str(t)
    pv.append(str(t))
print(tmp+ans[-1] if ans else "1")


for N in range(1,10**6+1):
    if N%1000 == 0:
        print(N)
    o = N
    ans = []
    while N > 0:
        i = 0
        while (i+2)*(i+1) <= 2*N:
            i += 1
        N -= (i+1)*i // 2
        ans.append("7"*i)
    tmp = ""
    n = 0
    pv = ["0"]
    for i in ans[:-1]:
        n = int(str(n)+i) % 7
        for t in range(1,7):
            for p in pv:
                if (n*10+t)%7==0 or int(p+i+str(t))%7==0:
                    break
            else:
                break
        else:
            break
        tmp += i + str(t)
        n = (n * 10 + t) % 7
        for p in range(len(pv)):
            pv[p] += i+str(t)
        pv.append(str(t))
    ori = tmp+ans[-1] if ans else "1"

    tmp += ans[-1]
    c = 0
    for i in range(len(tmp)):
        for j in range(i+1, len(tmp)+1):
            if int(tmp[i:j])%7 == 0:
                c += 1
    if c != o:
        print(o, ori, c)
        print(pv)
        print([int(i)%7 for i in pv])
        break