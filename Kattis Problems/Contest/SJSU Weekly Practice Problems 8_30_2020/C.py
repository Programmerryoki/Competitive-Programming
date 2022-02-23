n = int(input())
for a in range(n):
    b, p = input().split()
    b, p = int(b), float(p)

    miABPM = 60.0 * (b - 1) / p
    maABPM = 60.0 * (b + 1) / p
    BPM = 60*b / p
    # print("\n", b, p)
    print(miABPM, BPM, maABPM)