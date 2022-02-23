L = int(input())
D = int(input())
X = int(input())

N = L
Nd = sum([int(i) for i in str(N)])
while Nd != X:
    N += 1
    Nd = sum([int(i) for i in str(N)])
print(N)

M = D
Md = sum([int(i) for i in str(M)])
while Md != X:
    M -= 1
    Md = sum([int(i) for i in str(M)])
print(M)