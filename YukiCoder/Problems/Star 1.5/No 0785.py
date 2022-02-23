r = [int(i, 16) for i in input().split(",") if i != "NONE"]
g = [int(i, 16) for i in input().split(",") if i != "NONE"]
b = [int(i, 16) for i in input().split(",") if i != "NONE"]

R = [i for i in range(16) if i not in r]
G = [i for i in range(16) if i not in g]
B = [i for i in range(16) if i not in b]
print(len(R)**2 * len(G)**2 * len(B)**2)
# print(R,G,B)