from bisect import bisect_left

N,M = [int(i) for i in input().split()]
union = []
dic = {}
for _ in range(M):
    # print(union)
    # print(dic)
    L,R = [int(i) for i in input().split()]
    ind = bisect_left(union, L)
    if len(union) == 0:
        union.append(L)
        dic[L] = (L,R)
    if ind == 0:
        l,r = dic[union[0]]
        if R < l:
            union = [L] + union
            dic[L] = (L,R)
            continue
        n = None
        if L <= l <= R <= r:
            n = (l, R)
        elif L <= l <= r <= R:
            n = (l,r)
        union[0] = n[0]
        del dic[l]
        dic[n[0]] = n
    elif ind == len(union):
        l,r = dic[union[ind-1]]
        if r < L:
            union.append(L)
            dic[L] = (L,R)
            continue
        elif l <= L <= r <= R:
            n = (L,r)
        elif l <= L <= R <= r:
            n = (L,R)
        elif L <= l <= R <= r:
            n = (l, R)
        elif L <= l <= r <= R:
            n = (l,r)
        union[ind-1] = n[0]
        del dic[l]
        dic[n[0]] = n
    else:
        l,r = dic[union[ind-1]]
        n = None
        if r < L:
            l,r = dic[union[ind]]
            if R < l:
                union = [L] + union
                dic[L] = (L,R)
                continue
            n = None
            if l <= L <= r <= R:
                n = (L,r)
            elif l <= L <= R <= r:
                n = (L,R)
            elif L <= l <= R <= r:
                n = (l, R)
            elif L <= l <= r <= R:
                n = (l,r)
            union[ind] = n[0]
            del dic[l]
            dic[n[0]] = n
            continue
        elif l <= L <= r <= R:
            n = (L,r)
        elif l <= L <= R <= r:
            n = (L,R)
        elif L <= l <= R <= r:
            n = (l, R)
        elif L <= l <= r <= R:
            n = (l,r)
        union[ind-1] = n[0]
        del dic[l]
        dic[n[0]] = n
# print(union)
# print(dic)
print(N-len(union))