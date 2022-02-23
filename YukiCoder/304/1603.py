N,H,W = [int(i) for i in input().split()]
S = H+W-2
print((S)*((N // 2)*(N+(N&1)) // 2))