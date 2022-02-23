from itertools import accumulate

N = int(input())
S = input().split()
A = [int(S[i]) * i for i in range(N)]
S = input().split()
B = [int(S[i]) * i for i in range(N)]
CA = list(accumulate(A))
CB = list(accumulate(B))
print(CA, CB)
C = [0]*(2*N)
for i in range(N):
    C[i] = CA[i] + CB[i]
for i in range(N):
    C[2*N-i-1] = CA[N-i-1] + CB[N-i-1]
print(" ".join(str(i) for i in C))