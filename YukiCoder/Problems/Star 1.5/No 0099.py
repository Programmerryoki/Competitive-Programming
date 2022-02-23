N = int(input())
X = [int(i) for i in input().split()]
O, E = 0,0
for x in X:
    if x&1:
        O += 1
    else:
        E += 1
print(max(O,E) - min(O,E))