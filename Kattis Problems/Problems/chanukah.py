P = int(input())

for a in range(P):
    N = int(input().split()[1])
    print(a+1, int(0.5*N**2 + 1.5*N))

"""[2,5,9,14,20,27,35,44,54,65]"""