T = int(input())
for _ in range(T):
    N,line = input().split(); N = int(N)
    i = 0
    l = len(line)
    for j in range(N):
        lp = l
        if j%2==0:
            i += l//4
        l -= l//4
        if l == lp:
            break
    print(line[i:i+l])