T = int(input())
for case in range(T):
    N = int(input())
    L = [int(i) for i in input().split()]
    rev = 0
    for i in range(len(L)-1):
        j = L.index(min(L[i:]), i)
        rev += j - i + 1
        # print(i,j)
        L = L[:i] + L[i:j+1][::-1] + L[j+1:]
        # print(L)
    print("Case #"+str(case+1)+":",str(rev))