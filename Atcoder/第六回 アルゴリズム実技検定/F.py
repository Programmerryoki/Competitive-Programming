N,L,T,X = map(int, input().split())
total = 0
cont = 0
for _ in range(N):
    # print(total)
    A,B = map(int, input().split())
    if B < L:
        cont = 0
        total += A
        continue
    if cont + A < T:
        cont += A
        total += A
        continue
    if cont + A == T:
        cont = 0
        total += X + A
        continue
    if A > T:
        print("forever")
        exit()
    total += T - cont
    total += X + A
    cont = A
    if A == T:
        cont = 0
        total += X
    else:
        cont = A
print(total)