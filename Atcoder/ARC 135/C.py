N = int(input())
A = [int(i) for i in input().split()]
if not N&1:
    print(sum(A))
    exit()
ma = 30
counts = [0]*ma
for a in A:
    for i in range(ma):
        if a & 1 << i:
            counts[i] += 1
mv = sum(A)
for i in range(N):
    # print([bin(i)[2:][::-1] for i in A])
    # print(sum(A), N, counts)
    bi = bin(A[i])[2:][::-1]
    if counts[len(bi)-1] & 1:
        continue
    A = [j^A[i] for j in A]
    mv = max(mv, sum(A))
print(mv)