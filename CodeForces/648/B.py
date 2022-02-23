t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    sa = [i for i in A]
    sa.sort()
    B = [int(i) for i in input().split()]
    for i in range(n):
        try:
            j = A.index(sa[i], i)
            if i == j:
                continue
            else:
                if B[i] == B[j]:
                    if 1^B[i] not in B[i:]:
                        while B[i] == B[j]:
                            j = A.index(sa[i], j+1)
                A[i], A[j] = A[j], A[i]
                B[i], B[j] = B[j], B[i]
        except:
            print("No")
            break
    else:
        print("Yes")