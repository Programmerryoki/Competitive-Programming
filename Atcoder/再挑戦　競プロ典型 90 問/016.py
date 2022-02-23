N = int(input())
tmp = N
A,B,C = sorted([int(i) for i in input().split()], reverse=True)
minc = float("inf")
for i in range(-(-N//A)+1):
    for j in range(-(-N//B)+1):
        sab = i * A + j * B
        if sab > N:
            continue
        if (N - sab) % C != 0:
            continue
        k = (N - sab) // C
        if sab + k * C != N:
            continue
        c = i + j + k
        if c < minc:
            minc = c
print(minc)