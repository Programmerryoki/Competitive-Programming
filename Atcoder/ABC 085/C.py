N,Y = [int(i) for i in input().split()]
for i in range(N+1):
    for j in range(N-i, -1, -1):
        money = i*10000 + j*5000 + (N - i - j)*1000
        if money == Y:
            print(i,j,N-i-j)
            exit()
        elif money < Y:
            break
print(-1,-1,-1)