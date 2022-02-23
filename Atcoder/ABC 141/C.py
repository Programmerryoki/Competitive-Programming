N,K,Q = [int(i) for i in input().split()]
ppl = [0]*(N + 1)
for _ in range(Q):
    A = int(input())
    if A == 1:
        ppl[1] += 1
        if N != 2:
            ppl[-1] -= 1
    elif A == N:
        ppl[0] += 1
        if N != 2:
            ppl[-2] -= 1
    else:
        ppl[0] += 1
        ppl[A-1] -= 1
        ppl[A] += 1
        ppl[-1] -= 1
ans = ["Yes"] * N
ans[0] = "Yes" if ppl[0] < K else "No"
for i in range(1,N):
    ppl[i] += ppl[i-1]
    if ppl[i] >= K:
        ans[i] = "No"
print("\n".join(ans))