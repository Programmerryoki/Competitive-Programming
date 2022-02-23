n,X = map(int, input().split())
a = [int(i) for i in input().split()]
binX = bin(X)[2:]
binX = ("0"*(n-len(binX))+binX)[::-1]
print(sum([a[i] for i in range(n) if binX[i]=="1"]))