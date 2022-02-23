N,A,B = [int(i) for i in input().split()]
P,Q,R,S = [int(i) for i in input().split()]
ans = [["."]*(S - R + 1) for i in range(Q - P + 1)]
for i in range(P, Q+1):
    for j in range(R, S+1):
        k = i-A
        if j == B + k and max(1-A, 1-B) <= k <= min(N-A, N-B):
            ans[i-P][j-R] = "#"
        elif j == B - k and max(1-A, B-N) <= k <= min(N-A, B-1):
            ans[i-P][j-R] = "#"
print("\n".join("".join(i) for i in ans))