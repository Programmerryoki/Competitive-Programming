N,x = map(int, input().split())
A = [int(i) for i in input().split()]
A.sort()
c = 0
for i in range(N):
    x -= A[i]
    if x >= 0:
        c += 1
    if x <= 0:
        print(c)
        break
else:
    print(N - 1)