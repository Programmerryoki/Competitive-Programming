A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C,D = [int(i) for i in input().split()]
MA = [max(0, (C - A[1])), min(C, C - (C - A[1]))]
A[0], A[1] = A[0] - MA[0], max(0, A[1] - MA[1])
MB = [min(D, B[0] + MA[0]), max(0, D - (B[0] + MA[0]))]
# print(A,MA)
# print(B,MB)
print(A[0] + MB[0])