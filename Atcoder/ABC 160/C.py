K, N = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort()
D = [abs(A[(i+1)%N] - A[i]) for i in range(N-1)]
D.append(K - A[-1] + A[0])
print(sum(D) - max(D))
# Ar = [i for i in A]
# for i,a in enumerate(A):
#     if K - a < a:
#         Ar[i] = a - K
# print(min(max(A) - min(A), max(Ar) - min(Ar)))
