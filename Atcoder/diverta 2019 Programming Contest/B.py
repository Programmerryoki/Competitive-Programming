R,G,B,N = [int(i) for i in input().split()]
c = 0
for i in range(0,N+1,R):
    for j in range(0,N+1,G):
        if (N - i - j) < 0:
            break
        if (N - i - j)%B == 0:
            c += 1
print(c)