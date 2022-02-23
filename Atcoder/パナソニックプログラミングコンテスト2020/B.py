H, W = [int(i) for i in input().split()]
if H == 1 or W == 1:
    print(1)
else:
    if H%2 == 1 and W%2 == 1:
        print(H*W//2+1)
    else:
        print((H*W)//2)