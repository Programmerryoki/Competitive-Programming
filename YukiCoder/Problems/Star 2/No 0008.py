P = int(input())
for _ in range(P):
    N,K = [int(i) for i in input().split()]
    if N % (K+1) != 1 or K > N:
        print("Win")
    else:
        print("Lose")