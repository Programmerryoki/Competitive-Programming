M,N = [int(i) for i in input().split()]
if M == 1 or N == 1:
    print(1)
else:
    print(max(M,N) * -(-min(M,N)//2))