N,M = [int(i) for i in input().split()]
B = [[int(i) for i in input().split()] for _ in range(N)]
tmp = B[0][0]
if (tmp%7!=0 and tmp%7-1+M > 7) or (tmp%7==0 and M > 1) or (tmp == 0):
    print("No")
    exit()
for i in range(N):
    for j in range(M):
        B[i][j] -= tmp
        if B[i][j] != i*7 + j:
            print("No")
            exit()
print("Yes")