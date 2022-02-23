from collections import Counter

def count(A, ang):
    # ang = round(ang, 3)
    c = 0
    # num = 0
    for a in A:
        if abs(a%ang) <= 10**-6:
            c += a//ang
        else:
            c += a//ang - 1
    # return [c, num]
    return int(c)


T = int(input())
for case in range(T):
    N,D = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    ca = Counter(A)
    # print(ca.most_common(1))
    if ca.most_common(1)[0][1] >= D:
        print("Case #"+str(case+1)+": 0")
        continue

    lb = 0
    ub = 360*10**9
    nc = 0
    for i in range(50):
        mid = round((lb + ub) / 2, 5)
        nc = count(A, mid)
        if nc < D:
            ub = mid
        else:
            lb = mid
    print(lb, mid, ub)
    print("Case #"+str(case+1)+":",nc)