N,M = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
C.sort()
i = 0
while i < len(C) and M != 0:
    if C[i] <= M:
        M -= C[i]
        i += 1
    else:
        break
print(i)