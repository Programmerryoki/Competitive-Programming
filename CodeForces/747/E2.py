def mm(A,B):
    la = len(A); lb = len(B); lc = len(B[0])
    ans = [[0]*lc for i in range(la)]
    for i in range(la):
        for j in range(lc):
            for k in range(lb):
                ans[i][j] = A[i][k] * B[k][j]
    return ans

k = int(input())
n = int(input())


m = [[0,0,1,1,1,1],
     [0,0,1,1,1,1],
     [1,1,0,0,1,1],
     [1,1,0,0,1,1],
     [1,1,1,1,0,0],
     [1,1,1,1,0,0]]

mul = [m]
for i in range(k):
    mul