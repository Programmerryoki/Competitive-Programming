t = int(input())
for a in range(t):
    n = int(input())
    stores = [int(i) for i in input().split()]
    print((max(stores) - min(stores))*2)