N,M,C = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
c = 0
for _ in range(N):
    A = [int(i) for i in input().split()]
    if sum([A[i]*B[i] for i in range(M)] + [C]) > 0:
        c += 1
print(c)