dire = "NSEW"
move = [[0,1], [0,-1], [1,0], [-1,0]]

T = int(input())
for case in range(T):
    X,Y,M = input().split()
    pos = [int(X), int(Y)]
    ans = -1
    for t,C in enumerate(M,1):
        m = move[dire.index(C)]
        pos = [pos[0] + m[0], pos[1] + m[1]]
        if abs(pos[0]) + abs(pos[1]) <= t:
            ans = t
            break
    if ans != -1:
        print("Case #"+str(case+1)+":",ans)
    else:
        print("Case #"+str(case+1)+": IMPOSSIBLE")