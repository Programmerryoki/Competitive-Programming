D = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

mon = 0
mi = max(B)
pos = False

for a in range(len(A)):
    mon += A[a]
    if mon >= B[a]:
        pos = True
        mi = min(mi, B[a])
if pos:
    print(mi)
else:
    print(-1)