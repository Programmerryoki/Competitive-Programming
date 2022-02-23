from collections import defaultdict

N, t = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
if t == 1:
    for a in A:
        if 7777 - a in A:
            print("Yes")
            break
    else:
        print("No")
elif t == 2:
    if len(A) == len(set(A)):
        print("Unique")
    else:
        print("Contains duplicate")
elif t == 3:
    ca = defaultdict(int)
    valid = True
    for a in A:
        ca[a] += 1
        if len(ca) > N//2+1:
            print(-1)
            valid = False
            break
    if valid:
        ma = [0,0]
        for a in ca:
            if ca[a] > ma[1]:
                ma = [a,ca[a]]
        if ma[1] > N//2:
            print(ma[0])
        else:
            print(-1)
elif t == 4:
    A.sort()
    if len(A)%2 == 0:
        print(A[N//2-1],A[N//2])
    else:
        print(A[N//2])
elif t == 5:
    i = -1
    j = 0
    A.sort()
    for a in range(N):
        if A[a] < 100:
            i = a
        if A[a] <= 999:
            j = a
    print(" ".join(map(str, A[i+1:j+1])))