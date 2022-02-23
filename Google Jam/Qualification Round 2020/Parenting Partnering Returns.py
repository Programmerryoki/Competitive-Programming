T = int(input())
for case in range(T):
    time = [0,0]
    N = int(input())
    schedule = [[int(i) for i in input().split()] + [j] for j in range(N)]
    ans = [""]*N
    schedule.sort()
    for test in schedule:
        S, E, order = test
        if time[0] <= S:
            time[0] = E
            ans[order] = "C"
        elif time[1] <= S:
            time[1] = E
            ans[order] = "J"
        else:
            print("Case #"+str(case+1)+": IMPOSSIBLE")
            break
    else:
        print("Case #"+str(case+1)+":","".join(ans))
        continue