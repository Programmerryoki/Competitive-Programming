T = int(input())
for case in range(T):
    S = int(input())
    sen = {input() : 0 for i in range(S)}
    Q = int(input())
    c = 0
    n0 = S
    # prev = ""
    for a in range(Q):
        q = input()
        if sen[q] == 0:
            n0 -= 1
        sen[q] += 1
        # print(sen)
        # print(prev)
        if n0 == 0:
            for k in sen.keys():
                sen[k] = 0
            n0 = S
            sen[q] += 1
            # if prev != q:
            #     c += 1
            # prev = q
            c += 1
    print("Case #"+str(case+1)+":",c)