T = int(input())
for case in range(T):
    R,S = [int(i) for i in input().split()]
    print("Case #"+str(case+1)+":",(R-1)*(S-1))
    # D = [i for i in range(1,R+1)]*S
    ld = R*S
    # print(D)
    for n in range(R, 1, -1):
        for i in range(0,S-1):
            l = ld - n - i
            r = n-1
            # D = D[l:l+r] + D[:l] + D[l+r:]
            print(l, r)
            # print(D)
        ld -= S
    # print(D)