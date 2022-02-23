T = int(input())
for case in range(T):
    N = int(input())
    S = input()
    mdis = [float("inf")] * N
    mp = float("inf")
    for i in range(N):
        if S[i] == "1":
            mdis[i] = 0
            mp = i
        elif mp == float("inf"):
            continue
        else:
            mdis[i] = min(mdis[i], i - mp)
    mp = float("inf")
    for i in range(N-1,-1,-1):
        if S[i] == "1":
            mdis[i] = 0
            mp = i
        elif mp == float("inf"):
            continue
        else:
            mdis[i] = min(mdis[i], mp - i)
    print(f"Case #{case+1}: {sum(mdis)}")