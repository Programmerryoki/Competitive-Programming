while True:
    H,T = map(int, input().split())
    if H == 0 and T == 0:
        break
    if H == 1 and T == 0:
        print(-1)
        continue
    mm = 0
    if T&1:
        mm += 1
        T += 1
    if ((T//2) + H)&1:
        mm += 2
        T += 2
    T //= 2
    mm += T + (T + H) // 2
    print(mm)