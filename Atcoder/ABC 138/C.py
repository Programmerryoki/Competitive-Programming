N = int(input())
V = [int(i) for i in input().split()]
V.sort(reverse=True)
while len(V) != 1:
    a,b = V.pop(), V.pop()
    V.append((a+b)/2)
print(V[0])