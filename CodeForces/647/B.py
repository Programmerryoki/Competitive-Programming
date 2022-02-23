t = int(input())
for _ in range(t):
    n = int(input())
    S = set([int(i) for i in input().split()])
    for i in range(1,max(S)+1):
        test = set()
        for s in S:
            test.add(s^i)
        if S == test:
            print(i)
            break
    else:
        print(-1)