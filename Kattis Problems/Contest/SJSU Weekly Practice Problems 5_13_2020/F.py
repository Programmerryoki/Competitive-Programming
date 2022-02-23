N,B,H,W = [int(i) for i in input().split()]
price = [[int(input()), max([int(i) for i in input().split()])] for _ in range(H)]
price.sort()
for c, p in price:
    if p >= N and c*N <= B:
        print(c*N)
        break
else:
    print("stay home")