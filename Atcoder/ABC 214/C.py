N = int(input())
S = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]
S = S + S
T = T + T
time = [float("inf")]*N
time[0] = T[0]
for i in range(1, len(S)):
    time[i % N] = min(T[i], time[(i-1)%N] + S[i-1])
print("\n".join(str(i) for i in time))