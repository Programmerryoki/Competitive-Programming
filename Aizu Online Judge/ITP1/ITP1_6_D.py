n,m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]
b = [int(input()) for i in range(m)]
for row in a:
    print(sum([row[i]*b[i] for i in range(m)]))