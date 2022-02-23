from itertools import permutations

T = int(input())
for case in range(T):
    N,C = map(int, input().split())
    for per in permutations([i for i in range(1,N+1)], N):
        # print(per)
        L = list(per)
        rev = 0
        for i in range(len(L)-1):
            j = L.index(min(L[i:]), i)
            rev += j - i + 1
            L = L[:i] + L[i:j+1][::-1] + L[j+1:]
        print(rev,C,per)
        if rev == C:
            print("Case #"+str(case+1)+":"," ".join(map(str, per)))
            break
    else:
        print("Case #"+str(case+1)+": IMPOSSIBLE")