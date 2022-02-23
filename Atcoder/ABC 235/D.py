a, N = [int(i) for i in input().split()]
seen = {N}
mv = 0
que = [N]
while que:
    mv += 1
    tmp = []
    for n in que:
        nxt = str(n)[1:] + str(n)[0]
        if int(nxt) >= 10 and int(nxt)%10!=0:
            tmp.append(int(nxt))
        if n % a == 0:
            tmp.append(n//a)
    que.clear()
    for n in tmp:
        if n == 1:
            break
        if n not in seen:
            que.append(n)
            seen.add(n)
    else:
        continue
    break
else:
    print(-1)
    exit()
print(mv)