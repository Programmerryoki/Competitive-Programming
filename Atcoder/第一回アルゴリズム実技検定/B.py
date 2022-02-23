N = int(input())
f = int(input())
for i in range(N-1):
    A = int(input())
    print("stay" if A == f else "down "+str(abs(A - f)) if A < f else "up "+str(abs(A-f)))
    f = A