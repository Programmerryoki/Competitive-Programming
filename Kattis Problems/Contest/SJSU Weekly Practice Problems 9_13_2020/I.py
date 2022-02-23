T = int(input())
for case in range(T):
    n = int(input())
    v1 = [int(i) for i in input().split()]
    v2 = [int(i) for i in input().split()]
    v1.sort(); v2.sort(reverse=True)

    print("Case #" + str(case+1) + ":",sum([v1[i] * v2[i] for i in range(n)]))