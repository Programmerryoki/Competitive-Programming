N, p = [int(i) for i in input().split()]
problem = [int(i) for i in input().split()]

ttime = 0
ctime = 0
sol = 0

if problem[p] > 300:
    print("0 0")
else:
    ctime += problem[p]
    ttime += problem[p]
    sol += 1
    problem.pop(p)
    problem.sort()
    while ctime <= 300:
        t = problem.pop(0)
        if sol < N and t <= 300 - ctime:
            sol += 1
            ttime += ctime + t
            ctime += t
        else:
            break
    print(sol,ttime)