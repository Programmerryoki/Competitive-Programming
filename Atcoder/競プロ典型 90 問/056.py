N,S = [int(i) for i in input().split()]
price = []
dp = [[False] * (S+1) for i in range(N+1)]
dp[0][0] = True
for i in range(N):
    A,B = [int(i) for i in input().split()]
    price.append((A,B))
    for j in range(S):
        if dp[i][j]:
            if j+A <= S:
                dp[i+1][j+A] = True
            if j+B <= S:
                dp[i+1][j+B] = True
if dp[-1][-1] != True:
    print("Impossible")
    exit()

bag = ""
j = S
for i in range(N, 0, -1):
    A,B = price[i-1]
    if j-A >= 0 and dp[i-1][j-A] == True:
        bag += "A"
        j -= A
    elif j-B >= 0 and dp[i-1][j-B] == True:
        bag += "B"
        j -= B
print(bag[::-1])