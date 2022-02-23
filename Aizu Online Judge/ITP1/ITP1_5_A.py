while True:
    H,W = [int(i) for i in input().split()]
    if H == 0 == W:
        break
    for a in range(H):
        print("#"*W)
    print()