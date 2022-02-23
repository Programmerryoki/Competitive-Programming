N,M = map(int, input().split())
H = [int(i) for i in input().split()]
W = [int(i) for i in input().split()]
print(H)
hd = [H[i+1]-H[i] for i in range(len(H)-1)]
print(hd)
print(W)
