N,K = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]
P.sort()
print(sum(P[:K]))