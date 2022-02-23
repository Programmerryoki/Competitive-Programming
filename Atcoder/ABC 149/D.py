import math
N,K = [int(i) for i in input().split()]
R,S,P = [int(i) for i in input().split()]
T = input()
# ans = [0]*N
win = {"r":"p", "s":"r", "p":"s"}
point = {"r":R, "s":S, "p":P}
t = 0
for a in range(math.ceil(N/K)):
    h1 = sum([point[win[T[i]]] for i in range(a,N,2*K)])
    h2 = sum([point[win[T[i]]] for i in range(a+K,N,2*K)])
    print([point[win[T[i]]] for i in range(a,N,2*K)],[point[win[T[i]]] for i in range(a+K,N,2*K)])
    if h1 > h2:
        t += h1
    else:
        t += h2
print(t)