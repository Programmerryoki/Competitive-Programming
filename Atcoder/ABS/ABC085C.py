N,Y = [int(i) for i in input().split()]
for i in range(N+1):
    if i * 10000 > Y:
        break
    for j in range(N+1):
        if i * 10000 + j * 5000 > Y or i + j > N:
            break
        if i * 10000 + j * 5000 + (N - i - j) * 1000 == Y:
            print(i,j,N-i-j)
            exit()
print(-1,-1,-1)