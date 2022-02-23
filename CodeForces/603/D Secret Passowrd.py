n = int(input())
passw = [input() for i in range(n)]
passset = [set(passw[0])]
for a in range(1,len(passw)):
    s = set(passw[a])
    p = [len(s&i) > 0 for i in passset]
    su = sum(p)
    # print(su)
    if su == 0:
        passset.append(s)
    elif su >= 2:
        i = -1
        index = []
        while True:
            try:
                i = p.index(1, i+1)
                index.append(i)
                # print("i",i)
            except:
                break
        for i in index[::-1]:
            s = s | passset.pop(i)
        passset.append(s)


print(len(passset))