N,H,M,T = [int(i) for i in input().split()]
M += T*(N-1)
M,H = M%60, (H + M//60)%24
print("\n".join([str(H),str(M)]))