N,M,X = map(int, input().split())
books = []
for _ in range(N):
    C, *A = [int(i) for i in input().split()]
    books.append((C, A))

mincost = float("inf")
for n in range(2**N):
    num = bin(n)[2:]
    num = "0"*(N - len(num))+num
    xs = [0]*M
    cost = 0
    for i in range(N):
        if num[i] == "0":
            continue
        cost += books[i][0]
        for j,x in enumerate(books[i][1]):
            xs[j] += x
    if sum([x < X for x in xs]):
        continue
    mincost = min(mincost, cost)
print(mincost if mincost != float("inf") else -1)