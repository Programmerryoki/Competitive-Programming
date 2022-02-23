H,W = [int(i) for i in input().split()]
print(H*W if H == 1 or W == 1 else -(-H//2) * -(-W//2))