T = int(input())
for case in range(T):
    N,C = [int(i) for i in input().split()]
    intervals = []
    mr = -float("inf")
    ml = float("inf")
    for _ in range(N):
        L,R = [int(i) for i in input().split()]
        intervals.append((L,R))
        mr = max(mr, R, L)
        ml = min(ml, L, R)
    imos = [0]*(mr - ml + 1)
    for L,R in intervals:
        print(L,R, L-ml+1,R-ml)
        if L - ml + 1 >= len(imos):
            continue
        imos[L - ml + 1] += 1
        if R - mr < len(imos):
            imos[R - ml] -= 1
        # print(imos)
    # print(imos)
    for i in range(len(imos)-1):
        imos[i+1] += imos[i]
    # print(ml, imos, mr)
    imos.sort(reverse=True)
    ans = sum(imos[:C])
    print(f"Case #{case+1}: {ans + N}")