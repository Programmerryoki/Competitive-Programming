A,B,M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
p = min(A) + min(B)
for _ in range(M):
    x,y,c = map(int, input().split())
    p = min(p, A[x-1]+B[y-1]-c)
print(p)