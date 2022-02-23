T = int(input())
for case in range(T):
    N,D,C,M = [int(i) for i in input().split()]
    S = input()
    dogs = S.count("D")
    for i in range(N):
        if S[i] == "D" and D:
            dogs -= 1
            D -= 1
            C += M
        elif S[i] == "C" and C:
            C -= 1
        else:
            break
    print(f"Case #{case+1}: {'YES' if dogs == 0 else 'NO'}")